# Megaverse Creator

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Code Structure](#code-structure)
- [Error Handling and Resilience](#error-handling-and-resilience)
- [Rate Limiting](#rate-limiting)
- [Extensibility](#extensibility)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Introduction

This script is designed to create a Megaverse using the Crossmint API. It automates the process of building a 2D space filled with various astral objects like POLYanets, SOLoons, and comETHs according to a specified goal map.

## Features

- Asynchronous API calls for improved performance
- Rate limiting to respect API constraints
- Automatic retries with exponential backoff
- Dynamic creation of different astral objects (POLYanets, SOLoons, comETHs)
- Fetching and parsing of the goal map
- Error handling and logging

## Requirements

- Python 3.7+
- `aiohttp` library
- `asyncio` library

## Installation

1. Clone this repository:

```git clone https://github.com/yourusername/megaverse-creator.git```<br/>
```cd megaverse-creator```

2. Install the required packages:

```pip install aiohttp```

## How to Run

1. Open the script and replace the `candidate_id` in the `Megaverse` class with your own ID:
```python
self.candidate_id = "your-candidate-id-here"
```

2. Run the script:

```python 
megaverse_creator.py
```

The script will automatically fetch the goal map and start creating the Megaverse according to the specifications.

## Code Structure
- RateLimiter: Handles API rate limiting
- Megaverse: Main class for interacting with the Crossmint API
- make_request: Handles API requests with retries
- goal_map: Fetches the goal map
- fill_polyanets, fill_soloons, fill_comeths: Methods for creating specific astral objects
- fill: Determines which type of astral object to create
- build_megaverse: Orchestrates the creation of the entire Megaverse

## Error Handling and Resilience
- The script implements a retry mechanism with exponential backoff for failed API calls
- Rate limit responses (HTTP 429) are handled by waiting for the specified time before retrying
- Exceptions are caught and logged

## Rate Limiting
The RateLimiter class ensures that API calls are made within the specified rate limits (default: 2 requests per second).

## Extensibility
The code is designed to be easily extendable:
- New types of astral objects can be added by creating new methods in the Megaverse class
- The fill method can be expanded to handle new object types

## License
This project is open source and available under the MIT License.

```text
This README provides a comprehensive overview of your Megaverse Creator script, including how to run it, its features, and important details about its structure and functionality. You can adjust any sections as needed to better fit your specific implementation or add any additional information you think would be helpful for users of your script.
```
