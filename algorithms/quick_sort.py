def quick(arr):

    arr = arr.copy()

    comparisons = 0
    swaps = 0

    def quick_sort(low, high):

        nonlocal comparisons, swaps

        if low >= high:
            return

        pivot = arr[high]
        i = low

        for j in range(low, high):

            comparisons += 1

            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
                i += 1

            yield arr.copy(), comparisons, swaps

        arr[i], arr[high] = arr[high], arr[i]

        yield from quick_sort(low, i - 1)
        yield from quick_sort(i + 1, high)

    yield from quick_sort(0, len(arr) - 1)