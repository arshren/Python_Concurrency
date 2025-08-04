#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 17:53:03 2025

@author: renukhandelwal
"""
import time 
import multiprocessing
import psutil
import os

# Get the current process object
current_process = psutil.Process(os.getpid())

def cook_dish_processed(dish_name, duration):
    """A process function representing a chef in their own kitchen."""
    print(f"[Process] Chef in their own kitchen starts cooking {dish_name} for {duration}s.")
    time.sleep(duration) # This time is spent on the chef's dedicated core.
    print(f"[Process] Chef finishes cooking {dish_name}.")

def multiprocessing_example():
    print("\n--- Starting Multiprocessing Example ---")
    print("Three Chefs (Processes) start cooking in their own kitchens...")
    
    # --- Capture initial resource usage ---
    initial_cpu_times = current_process.cpu_times()
    initial_memory = current_process.memory_info().rss
    # Record the start time
    start_time = time.perf_counter()
    
    dishes = [("Salad", 20), ("Main Course", 30), ("Dessert", 50)]
    processes = []
    
    # Each chef (process) is given a dish and a kitchen (core).
    # They cook in parallel, not just concurrently.
    for dish_name, duration in dishes:
        process = multiprocessing.Process(target=cook_dish_processed, args=(dish_name, duration))
        processes.append(process)
        process.start()

    # The main kitchen waits for all the other kitchens to finish.
    for process in processes:
        process.join()
    # --- Capture final resource usage ---
    end_time = time.perf_counter()
    final_cpu_times = current_process.cpu_times()
    final_memory = current_process.memory_info().rss
    
    # --- Calculate and display results ---
    total_time = end_time - start_time
    cpu_user_time_diff = final_cpu_times.user - initial_cpu_times.user
    cpu_system_time_diff = final_cpu_times.system - initial_cpu_times.system
    memory_increase_mb = (final_memory - initial_memory) / (1024 * 1024)
    
    print(f"Total time taken to cook all dishes: {total_time:.2f} seconds.")    
    print(f"CPU User Time: {cpu_user_time_diff:.4f} seconds")
    print(f"CPU System Time: {cpu_system_time_diff:.4f} seconds")
    print(f"Memory Increase (Peak): {memory_increase_mb:.2f} MB")
    print("--- All dishes are finished. Multiprocessing example complete. ---")

if __name__ == "__main__":
    multiprocessing_example()