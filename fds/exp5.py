"""
Write a python program to store 2d year percentage of students in an array.
Write function for sorting array of floating point numbers in ascending
order using:
1. insertion sort
2. shell sort and display top 5 sortes.
"""

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

def shell_sort(array):
    length = len(array)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2
    return array

score_array = []
print("Press q or quit to exit")
while True:
    score = input("Enter student score:")
    if score.lower() in ['q', 'quit']:
        break
    else:
        score_array.append(float(score))
print("\nBefore sorting:\n", score_array)
print("After insertion sort:\n", insertion_sort(score_array.copy()))
print("After shell sort:\n", shell_sort(score_array.copy()))
print("\nTop 5 values after sort:")
if len(score_array) <= 5:
    print(shell_sort(score_array))
else:
    print(shell_sort(score_array)[:5])

