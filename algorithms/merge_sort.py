def merge(arr):

    arr = arr.copy()

    comparisons = 0
    swaps = 0

    def merge_sort(l, r):

        nonlocal comparisons, swaps

        if r - l <= 1:
            return

        m = (l + r) // 2

        yield from merge_sort(l, m)
        yield from merge_sort(m, r)

        left = arr[l:m]
        right = arr[m:r]

        i = j = 0
        k = l

        while i < len(left) and j < len(right):

            comparisons += 1

            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            swaps += 1
            k += 1

            yield arr.copy(), comparisons, swaps

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            swaps += 1
            yield arr.copy(), comparisons, swaps

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            swaps += 1
            yield arr.copy(), comparisons, swaps

    yield from merge_sort(0, len(arr))