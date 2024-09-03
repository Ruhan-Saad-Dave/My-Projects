"""
Write a python program to store 1st year percentage of students array. Write
function for sorting array of floating point numbers in ascending order 
using quicksort and display top 5 scores.
"""

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    right = [x for x in array if x > pivot]
    mid = [x for x in array if x == pivot]
    return quick_sort(left) + mid + quick_sort(right)

score_array = []
print("Press q or quit to exit")
while True:
    score = input("Enter student score:")
    if score.lower() in ['q', 'quit']:
        break
    else:
        score_array.append(float(score))

print("\nBefore sorting:\n", score_array)
print("After insertion sort:\n", quick_sort(score_array))
print("\nTop 5 values after sort:")
if len(score_array) <= 5:
    print(quick_sort(score_array))
else:
    print(quick_sort(score_array)[:5])