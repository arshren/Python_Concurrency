#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 17:50:46 2025

@author: renukhandelwal
"""

import time
import threading
import psutil
import os

# Get the current process object
current_process = psutil.Process(os.getpid())

def cook_dish_threaded(dish_name, duration):
    """A threaded function representing the chef preparing a dish."""
    print(f"[Thread] Chef starts preparing {dish_name} for {duration}s.")
    time.sleep(duration) # Simulate waiting (e.g., the pot is boiling)
    print(f"[Thread] Chef finishes preparing {dish_name}.")

def multithreading_example():
    print("--- Starting Multithreading Example ---")
    print("One Chef (Main Process) starts preparing 3 dishes...")
    
    # --- Capture initial resource usage ---
    initial_cpu_times = current_process.cpu_times()
    initial_memory = current_process.memory_info().rss
    # Record the start time
    start_time = time.perf_counter()
    dishes = [("Salad", 20), ("Main Course", 30), ("Dessert", 50)]
    threads = []
    
    # The chef starts each dish and then immediately starts the next one.
    # The OS handles the switching between tasks when one is waiting.
    for dish_name, duration in dishes:
        thread = threading.Thread(target=cook_dish_threaded, args=(dish_name, duration))
        threads.append(thread)
        thread.start()

    # The chef waits until all the dishes are finished.
    for thread in threads:
        thread.join()
    # --- Capture final resource usage ---
    end_time = time.perf_counter()
    final_cpu_times = current_process.cpu_times()
    final_memory = current_process.memory_info().rss
    
    # --- Calculate and display results ---
    total_time = end_time - start_time
    cpu_user_time_diff = final_cpu_times.user - initial_cpu_times.user
    cpu_system_time_diff = final_cpu_times.system - initial_cpu_times.system
    memory_increase_mb = (final_memory - initial_memory) / (1024 * 1024)

    print("--- All dishes are finished. Multithreading example complete. ---")
    print(f"Total time taken to cook all dishes: {total_time:.2f} seconds.")
    print(f"CPU User Time: {cpu_user_time_diff:.4f} seconds")
    print(f"CPU System Time: {cpu_system_time_diff:.4f} seconds")
    print(f"Memory Increase (Peak): {memory_increase_mb:.2f} MB")
    print("--- All dishes are finished. Multithreading example complete. ---")
multithreading_example()