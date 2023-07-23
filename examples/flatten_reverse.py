def flatten(array: list):
    flat_array = list()
    for element in array:
        if isinstance(element, (list, tuple, set, frozenset, dict)):
            flat_array += flatten(element)
        else:
            flat_array.append(element)

    return flat_array


def reverse_whole_elements(array: list):
    reversed_array = array.copy()
    reversed_array = reversed_array[::-1]
    for element in reversed_array:
        if isinstance(element, list):
            reversed_array[reversed_array.index(element)] = reverse_whole_elements(element)

    return reversed_array


def test(test_input, func):
    print(f"THE TEST INPUT: {test_input}")
    print("-------------------------------------------------------------")
    print(f"THE {func.__name__} RESULT: {func(test_input)}")
    print("-------------------------------------------------------------")

if __name__ == '__main__':
    flatten_test_input = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
    reverse_test_input = [[1, 2], [3, 4], [5, 6, 7]]

    test(flatten_test_input, flatten)
    test(reverse_test_input, reverse_whole_elements)
