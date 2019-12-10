def max_profit(arr):
    """
        The function receives a list-type parameter.
        It starts from the second-lowest value index. 
        If it finds a larger value, it returns the largest 
        minus the smallest value. If no, return the value of 0.
    """
    min_value = min(arr)
    max_value = min_value
    index = arr.index(min_value)
    for i in arr[index+1:]:
        if max_value < i:
            max_value = i

    if max_value == min_value:
        max_value = 0
        return max_value

    result = max_value - min_value
    return result
