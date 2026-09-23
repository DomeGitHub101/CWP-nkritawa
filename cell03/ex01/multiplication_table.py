#!/usr/bin/env python3

print("Enter a number")
number = int(input())
multiplier = 0

while multiplier <= 9:
    print(f"{multiplier} x {number} = {multiplier * number}")
    multiplier += 1
