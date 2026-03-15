def linear_search(arr, target):

    for i in range(len(arr)):

        yield ("compare", i)

        if arr[i] == target:
            yield ("found", i)
            return i

    yield ("not_found", -1)