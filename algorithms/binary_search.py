def binary_searchl(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        yield ("check_middle", mid)

        if arr[mid] == target:
            yield ("found", mid)
            return mid

        elif arr[mid] < target:
            yield ("go_right", mid)
            left = mid + 1

        else:
            yield ("go_left", mid)
            right = mid - 1

    yield ("not_found", -1)