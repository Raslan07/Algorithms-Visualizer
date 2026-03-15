def merge(arr):
    arr = arr.copy()
    comparisons = 0
    swaps = 0

    yield from _merge_sort(arr, 0, len(arr) - 1, comparisons, swaps)
    yield arr, comparisons, swaps, ()


def _merge_sort(arr, left, right, comparisons, swaps):
    if left >= right:
        return

    mid = (left + right) // 2

    yield from _merge_sort(arr, left, mid, comparisons, swaps)
    yield from _merge_sort(arr, mid + 1, right, comparisons, swaps)
    yield from _merge(arr, left, mid, right, comparisons, swaps)


def _merge(arr, left, mid, right, comparisons, swaps):
    left_part  = arr[left : mid + 1]
    right_part = arr[mid + 1 : right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        comparisons += 1
        li = left + i
        rj = mid + 1 + j
        yield arr, comparisons, swaps, (li, rj)   # ← highlight compared pair

        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
            swaps += 1

        k += 1
        yield arr, comparisons, swaps, (k - 1, k - 1)

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1
        yield arr, comparisons, swaps, (k - 1,)

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1
        yield arr, comparisons, swaps, (k - 1,)