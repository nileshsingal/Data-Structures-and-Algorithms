def bubble_sort(arr):
    n = len(arr)

    # Bubble sort
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("After Using Bubble Sort:")
    print(arr)

if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    print("Before Using Bubble Sort:")
    print(arr)

    bubble_sort(arr)
