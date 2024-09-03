"""
1. Write a python program to store student roll numbers in array who attended 
training program in random order. Write function for searching whether particular 
student attended training program or not using linear search and sentinal search.
2. Write a python program to store roll number of students of array who attending 
training program in sorted order. Write function for searching whether particular
student attendees training program or not using binary search and fibonacci search
"""

import random

def linear_search(array, target):
    for index in range(len(array)):
        if target == array[index]:
            print(f"Target {target} found at index: {index}")
            break
    else:
        print(f"Target {target} not found!")

def sentinal_search(array, target):
    length = len(array)
    last = array[length - 1]
    array[length - 1] = target
    index = 0
    while array[index] != target:
        index += 1
    array[length - 1] = last
    if (index < length - 1) or array[length - 1] == target:
        print(f"Target {target} is found at index: {index}")
    else:
        print(f"Target {target} not found!")

def binary_search(array, target):
    found, low = 0, 0
    high = len(array) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == target:
            print(f"Target {target} found at index: {mid}")
            found = 1
            break
        elif array[mid] > target:
            high = mid - 1
        else: 
            low = mid + 1
    if found == 0:
        print(f"Target {target} not found!")

def fibonacci_search(array, target):
    found, fib2, fib1 = 0, 0, 1
    fib = fib1 + fib2
    length = len(array)
    while fib < length:
        fib2 = fib1
        fib1 = fib 
        fib = fib1 + fib2 
    offset = -1
    while fib > 1:
        index = min(offset + fib2, length - 1)
        if array[index] < target:
            fib = fib1 
            fib1 = fib2 
            fib2 = fib - fib1 
            offset = index 
        elif array[index] > target:
            fib = fib2 
            fib1 = fib1 - fib2 
            fib2 = fib - fib1 
        else:
            print(f"Target {target} found at index: {index}")
            found = 1
            break
    if fib1 and offset < (length - 1) and array[offset + 1] == target:
        print(f"Target {target} found at index: {offset + 1}")
        found = 1
    if found == 0:
        print(f"Target {target} not found!")
    
array = []
print("press q or quit to exit")
while True:
    roll = input("Enter student roll number:")
    if roll.lower() in ['q', 'quit']:
        break
    else:
        array.append(int(roll))
print(array)
for i in range(len(array)):
    for j in range(len(array) - 1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
sorted_array = []
for roll in array:
    if roll not in sorted_array:
        sorted_array.append(roll)
print(sorted_array)
random_array = sorted_array.copy()
random.shuffle(random_array)
print(random_array)
print(sorted_array)

value = int(input("Enter the number to search for:"))
print("\nLinear search:")
linear_search(random_array, value)
print("\nSentinal search:")
sentinal_search(random_array, value)
print("\nbinary search:")
binary_search(sorted_array, value)
print("\nfibonacci search:")
fibonacci_search(sorted_array, value)
