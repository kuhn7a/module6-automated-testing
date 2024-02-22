def only_odd_numbers(arr):
    if not isinstance(arr, list):
        return []
    # iterating each number in list
    output_arr = []
    for num in arr:
        # if number isn't cleanly divisible by 2, the number is odd
        if num % 2 != 0:
            output_arr.append(num)
    return output_arr


def only_even_numbers(arr):
    if not isinstance(arr, list):
        return []
    # iterating through each number in list
    output_arr = []
    for num in arr:
        # if number has remainder of 0, then the number is even
        if num % 2 == 0:
            output_arr.append(num)
    return output_arr
