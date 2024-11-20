import asyncio
import aiohttp
import time

class RateLimiter:
    def __init__(self, rate_limit=1, time_period=1):
        self.rate_limit = rate_limit
        self.time_period = time_period
        self.calls = []

    async def wait(self):
        now = time.time()
        self.calls = [call for call in self.calls if now - call < self.time_period]
        if len(self.calls) >= self.rate_limit:
            await asyncio.sleep(self.time_period - (now - self.calls[0]))
        self.calls.append(time.time())



class Megaverse:
    def __init__(self):
        self.candidate_id = "c0206b6c-ebc1-4f00-afb3-85f96a75f5a4"
        self.base_url = "https://challenge.crossmint.io/api"
        self.headers = {
        'Content-Type': 'application/json'
        }
        self.payload = {
            "row": 0, 
            "column": 0, 
            "candidateId": self.candidate_id
        }
        self.rate_limiter = RateLimiter(rate_limit=2, time_period=1)

    async def make_request(self, url, payload):
        max_retries = 5
        for attempt in range(max_retries):
            try:
                await self.rate_limiter.wait()
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=self.headers, json=payload) as response:
                        if response.status == 429:
                            retry_after = int(response.headers.get('Retry-After', 3))
                            print(f"Rate limit exceeded. Waiting for {retry_after} seconds.")
                            await asyncio.sleep(retry_after)
                            continue
                        return await response.json()
            except Exception as e:
                if attempt == max_retries - 1:
                    return f"Failed after {max_retries} attempts: {e}"
                await asyncio.sleep(2 ** attempt)


    async def goal_map(self):
        try:
            goal_url = self.base_url + "/map/" + self.candidate_id + "/goal"
            async with aiohttp.ClientSession() as session:
                async with session.get(goal_url, headers=self.headers) as response:
                    if response.status == 200:
                        data = await response.json()
                        return data["goal"]
                    else:
                        return f"Failed to retrieve goal map: HTTP {response.status}"
        
        except Exception as e:
            return f"Failed to retrieve goal map: {e}"

    async def fill_polyanets(self, x, y):
        url = f"{self.base_url}/polyanets"
        self.payload["row"] = x
        self.payload["column"] = y
        return await self.make_request(url, self.payload)
    
    async def fill_soloons(self, x, y, color):
        url = f"{self.base_url}/soloons"
        self.payload["row"] = x
        self.payload["column"] = y
        self.payload["color"] = color.lower()
        return await self.make_request(url, self.payload)
        
    async def fill_comeths(self, x, y, direction):
        url = f"{self.base_url}/comeths"
        self.payload["row"] = x
        self.payload["column"] = y
        self.payload["direction"] = direction.lower()
        return await self.make_request(url, self.payload)

    async def fill(self, x, y, fill_string):
        fill_type = ""
        argument = ""
        if "_" in fill_string:
            argument = fill_string.split("_")[0]
            fill_type = fill_string.split("_")[1]
        else:
            fill_type = fill_string

        match fill_type:
            case "POLYANET":
                response = await self.fill_polyanets(x, y)
                print("polyanet", response, x, y)

            case "SOLOON":
                response = await self.fill_soloons(x, y, argument)
                print("soloon", response, x, y)

            case "COMETH":
                response = await self.fill_comeths(x, y, argument)
                print("cometh", response, x, y)

            case "SPACE":
                pass
        
    async def build_megaverse(self):
        goal_map = await self.goal_map()
        for i in range(len(goal_map[0])):
            for j in range(len(goal_map)):
                await self.fill(i, j, goal_map[i][j])


megaverse = Megaverse()
asyncio.run(megaverse.build_megaverse())

    

    
