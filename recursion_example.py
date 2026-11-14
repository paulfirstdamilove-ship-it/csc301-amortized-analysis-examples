#!/usr/bin/env python3
"""
CSC 301 - Recursion Example
Student: Akerele Paul Bayo
Matric: 240502023
"""

def factorial(n):
    """Calculate factorial of n using recursion"""
    if n == 0 or n == 1:          # Base case
        return 1
    else:
        return n * factorial(n - 1)   # Recursive case

# Test the function
print("Factorial of 5 =", factorial(5))
print("Factorial of 7 =", factorial(7))
print("Factorial of 0 =", factorial(0))
