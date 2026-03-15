def insertion(arr):
    arr = arr.copy()
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            comparisons += 1
            yield arr, comparisons, swaps, (j, j + 1)   # ← highlight

            arr[j + 1] = arr[j]
            swaps += 1
            j -= 1
            yield arr, comparisons, swaps, (j + 1, j + 2) if j >= 0 else (0, 1)

        arr[j + 1] = key
        comparisons += 1
        yield arr, comparisons, swaps, (j + 1, i)

    yield arr, comparisons, swaps, ()