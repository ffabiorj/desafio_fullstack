
def try_correct_order(string_to_test):
    """
        The function receives a string parameter.
        it proceeds to check if the number of characters after
        the string division is even. If so, it Goes through the array 
        starting from half of the string to try to find your partner.
    """
    size_string = len(string_to_test)
    if size_string % 2 != 0 or size_string == 0:
        return 'NÃO'
    for element, i in enumerate(string_to_test[int(size_string / 2):]):
        expected_pair = string_to_test[int(size_string / 2) - element - 1]
        if i in ['{', '[', '(']:
            return 'NÃO'
        if i == '}':
            if expected_pair != '{':
                return 'NÃO'
        if i == ')':
            if expected_pair != '(':
                return 'NÃO'
        if i == ']':
            if expected_pair != '[':
                return 'NÃO'
    return 'SIM'
