def sum_two_numbers(arr, target):
    """
       The function receives two parameters, a list and a target. 
       it goes through the list and checks if the sum of two numbers
       is equal to the target and returns their index.
    """
    number_list = []
    for index1, i in enumerate(arr):
        for index2, k in enumerate(arr[index1+1:]):
            if i + k == target:
                number_list.append(arr.index(i))
                number_list.append(arr.index(k))
    return number_list
