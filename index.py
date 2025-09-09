# # put the elements to their right places
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]           # pick the current element
        j = i - 1
        while j >= 0 and arr[j] > key:  # shift larger elements
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key        # insert key at correct position


array = [12,3,1,34,67,2,5]
insertion_sort(array)
print(array)