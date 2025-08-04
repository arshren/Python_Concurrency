#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 17:47:57 2025

@author: renukhandelwal
"""
import time
import asyncio
import psutil
import os

# Get the current process object
current_process = psutil.Process(os.getpid())

async def cook_dish_async(dish_name, duration):
    """An asynchronous coroutine representing the chef cooking a dish."""
    print(f"[Async] The efficient chef starts preparing {dish_name} for {duration}s.")
    await asyncio.sleep(duration) # The chef cooperatively "awaits" this task and moves on to another one.
    print(f"[Async] The efficient chef finishes preparing {dish_name}.")

async def asyncio_example():
    print("\n--- Starting Asyncio Example ---")
    print("One efficient chef (single thread) starts preparing 3 dishes...")
    
     # --- Capture initial resource usage ---
    initial_cpu_times = current_process.cpu_times()
    initial_memory = current_process.memory_info().rss
    start_time = time.perf_counter()  # Record the start time
    
    dishes = [("Salad", 20), ("Main Course", 30), ("Dessert", 50)]
    tasks = []
    
    # The chef adds all the dishes to their mental to-do list (the event loop).
    for dish_name, duration in dishes:
        task = asyncio.create_task(cook_dish_async(dish_name, duration))
        tasks.append(task)
    
    # The chef starts working on all dishes at once.
    await asyncio.gather(*tasks)

   
     # Record the end time
     # --- Capture final resource usage ---
    end_time = time.perf_counter()
    final_cpu_times = current_process.cpu_times()
    final_memory = current_process.memory_info().rss
    
    # --- Calculate and display results ---
    total_time = end_time - start_time
    cpu_user_time_diff = final_cpu_times.user - initial_cpu_times.user
    cpu_system_time_diff = final_cpu_times.system - initial_cpu_times.system
    memory_increase_mb = (final_memory - initial_memory) / (1024 * 1024)
    
   

    print("--- All dishes are finished. Asyncio example complete. ---")
    print(f"Total wall clock time taken to cook all dishes: {total_time:.2f} seconds.")
    print(f"CPU User Time: {cpu_user_time_diff:.4f} seconds")
    print(f"CPU System Time: {cpu_system_time_diff:.4f} seconds")
    print(f"Memory Increase (Peak): {memory_increase_mb:.2f} MB")
asyncio.run(asyncio_example())