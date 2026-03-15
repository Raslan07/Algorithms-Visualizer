def bubble(arr):

    arr = arr.copy()
    n = len(arr)

    comparisons = 0
    swaps = 0

    for i in range(n):
        for j in range(n - i - 1):

            comparisons += 1

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

            yield arr.copy(), comparisons, swaps