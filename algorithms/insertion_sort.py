def insertion(arr):

    arr = arr.copy()

    comparisons = 0
    swaps = 0

    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:

            comparisons += 1

            arr[j + 1] = arr[j]
            swaps += 1

            j -= 1

            yield arr.copy(), comparisons, swaps

        arr[j + 1] = key

        yield arr.copy(), comparisons, swaps