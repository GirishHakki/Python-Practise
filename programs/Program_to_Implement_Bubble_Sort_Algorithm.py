def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


my_array = [64, 25, 12, 22, 11]
bubble_sort(my_array)
print("Sorted array using Bubble Sort:", my_array)