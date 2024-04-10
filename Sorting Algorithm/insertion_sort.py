def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

    print("After insertion sort:")
    for num in arr:
        print(num, end=" ")
    print()

if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    print("Before using insertion Sort:")
    for num in arr:
        print(num, end=" ")
    print()
    insertion_sort(arr)

