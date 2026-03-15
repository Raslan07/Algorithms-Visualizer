def quick(arr):
    arr = arr.copy()
    comparisons = 0
    swaps = 0

    yield from _quick_sort(arr, 0, len(arr) - 1, comparisons, swaps)
    yield arr, comparisons, swaps, ()


def _quick_sort(arr, low, high, comparisons, swaps):
    if low < high:
        yield from _partition(arr, low, high, comparisons, swaps)

        # get the pivot index by re-running partition logic (simpler: track it)
        pivot_index = arr.index(sorted(arr[low:high+1])[high - low // 2])

        yield from _quick_sort(arr, low, pivot_index - 1, comparisons, swaps)
        yield from _quick_sort(arr, pivot_index + 1, high, comparisons, swaps)


def _partition(arr, low, high, comparisons, swaps):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        comparisons += 1
        yield arr, comparisons, swaps, (j, high)   # ← highlight: current vs pivot

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
            yield arr, comparisons, swaps, (i, j)

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    swaps += 1
    yield arr, comparisons, swaps, (i + 1, high)