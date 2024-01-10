# Declaring an empty list
arr = []

# Asking the user the array length
size = int(input("What is the size of your array? "))

# Taking all the array elements
for _ in range(size):
    element = int(input("Enter element: "))
    arr.append(element)

# Method to display the elements
def display_elements(arr):
    for element in arr:
        print(element)

# Defining a bubble sort method
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    display_elements(arr)

# Defining an insertion sort method
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    display_elements(arr)

# Defining a selection sort method
def selection_sort(arr):
    size = len(arr)
    for i in range(size):
        min_idx = i
        for j in range(i+1, size):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    display_elements(arr)

# Defining a merge method
def merge(left, right):
    result = []
    index_left = index_right = 0

    while index_left < len(left) and index_right < len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

    # Add the remaining elements from left and right (if any)
    result.extend(left[index_left:])
    result.extend(right[index_right:])
    
    return result


# Defining a merge sort method
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    midpoint = len(arr) // 2

    left = merge_sort(arr[:midpoint])
    right = merge_sort(arr[midpoint:])

    return merge(left, right)
   
# Defining a quick sort method
from random import randint
def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[randint(0, len(arr)-1)]
    low = [item for item in arr if item < pivot]
    same = [item for item in arr if item == pivot]
    high = [item for item in arr if item > pivot]

    return quick_sort(low) + same + quick_sort(high)

# Structural pattern matching
algo = int(input("Select a sorting algorithm to sort your array:\n 1. Bubble Sort\n 2. Insertion Sort\n 3. Selection Sort\n 4. Merge Sort\n 5. Quick Sort\n"))
match algo:
    case 1:
        bubble_sort(arr)
    case 2:
        insertion_sort(arr)
    case 3:
        selection_sort(arr)
    case 4:
        display_elements(merge_sort(arr))
    case 5:
        display_elements(quick_sort(arr))
    case _:
        print("ERROR! Please select an appropriate option.")
