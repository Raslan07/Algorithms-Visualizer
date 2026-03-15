def bubble(arr):
    arr = arr.copy()
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            yield arr, comparisons, swaps, (j, j + 1)   # ← highlight these two

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                yield arr, comparisons, swaps, (j, j + 1)

    yield arr, comparisons, swaps, ()   # no highlight when done