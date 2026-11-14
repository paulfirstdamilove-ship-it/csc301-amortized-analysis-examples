#!/usr/bin/env python3
"""
CSC 301 - Dynamic Array Example
Student: Akerele Paul Bayo
Matric: 240502023

Python lists are dynamic arrays. They automatically resize when full.
This is a classic example where amortized analysis is applied.
"""

def demonstrate_dynamic_array():
    arr = []
    print("Demonstrating Dynamic Array (Python list):\n")

    for i in range(1, 11):
        arr.append(i)
        print(f"Inserted {i:2d} | Current array: {arr} | Length: {len(arr)}")

    print("\nNote: When the internal capacity is exceeded, Python automatically")
    print("resizes the array (usually doubles it). This expensive operation")
    print("happens rarely, so the amortized cost of each append is O(1).")

if __name__ == "__main__":
    demonstrate_dynamic_array()
