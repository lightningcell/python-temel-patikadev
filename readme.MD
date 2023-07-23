# Examples

1. **Write a function that flattens a list.**

    ### Function:
    ```python
   def flatten(array: list):
        flat_array = list()
        for element in array:
            if isinstance(element, (list, tuple, set, frozenset, dict)):
                flat_array += flatten(element)
            else:
                flat_array.append(element)
    
        return flat_array

   ```
   
    ### Outputs
   ```shell
    THE TEST INPUT: [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
    -------------------------------------------------------------
    THE flatten RESULT: [1, 'a', 'cat', 2, 3, 'dog', 4, 5]
    -------------------------------------------------------------
   ```
   
2. **Write a function that reverses the elements inside the given list. If the elements inside the list also contain the list, reverse their elements as well.**

    ### Function:
    ```python
   def reverse_whole_elements(array: list):
        reversed_array = array.copy()
        reversed_array = reversed_array[::-1]
        for element in reversed_array:
            if isinstance(element, list):
                reversed_array[reversed_array.index(element)] = reverse_whole_elements(element)

        return reversed_array

   ```
   
    ### Outputs
   ```shell
    THE TEST INPUT: [[1, 2], [3, 4], [5, 6, 7]]
    -------------------------------------------------------------
    THE reverse_whole_elements RESULT: [[7, 6, 5], [4, 3], [2, 1]]
    -------------------------------------------------------------
   ```
    