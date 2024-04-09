def selection_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        min_index = i

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

print(selection_sort([5, 3, 4, 3, 1]))  # Output: [1, 3, 3, 4, 5]
