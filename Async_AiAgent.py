#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 18:56:14 2025

@author: renukhandelwal
"""

import asyncio
import aiohttp
import json
from typing import List, Dict

class AIAgent:
    def __init__(self):
        self.tools = {
            'weather': self.get_weather,
            'search': self.web_search,
            'database': self.query_database
        }
    
    async def get_weather(self, location: str) -> Dict:
        """Simulate weather API call"""
        #async with aiohttp.ClientSession() as session:
            # This would be a real API call
        print(f"Getting Weather for {location}")
        await asyncio.sleep(5)  # Simulate network delay
        return {"location": location, "temp": "22°C", "condition": "sunny"}
    
    async def web_search(self, query: str) -> Dict:
        """Simulate web search API call"""
        #async with aiohttp.ClientSession() as session:
        print(f" Searching web for --->{query}")
        await asyncio.sleep(10)  # Simulate network delay
        return {"query": query, "results": ["result1", "result2", "result3"]}
    
    async def query_database(self, query: str) -> Dict:
        """Simulate database query"""
        print(f"Query database -->{query}")
        await asyncio.sleep(8)  # Simulate DB query time
        return {"query": query, "data": ["record1", "record2"]}
    
async def handle_user_request_concurrent(agent, user_input: str):
    """Process multiple tools simultaneously"""
    start_time = asyncio.get_event_loop().time()
    
    # These run concurrently
    tasks = [
        agent.get_weather("New York"),
        agent.web_search("AI news"),
        agent.query_database("SELECT * FROM users")
    ]
    
    # Wait for all tasks to complete
    weather, search_results, db_data = await asyncio.gather(*tasks)
    print(f"Weather for {weather['location']} is {weather['temp']} and conditionsa are {weather['condition']}\n")
    print(f"Searching Web for --->{search_results['query']} and results -> {search_results['results']}\n")
    print(f"Database Query--->{db_data['query']} and results {db_data['data']}\n")
    end_time = asyncio.get_event_loop().time()
    print(f"Concurrent execution took: {end_time - start_time:.2f} seconds")
    
    return {
        "weather": weather,
        "search": search_results,
        "database": db_data
    }
async def main():
    agent = AIAgent()
    print("\nTesting concurrent execution:")
    await handle_user_request_concurrent(agent, "Get me updates")
if __name__ == "__main__":
    asyncio.run(main())   
    