
def binary_search(arr, element_to_find):

    left_index = 0
    right_index = len(arr) - 1
    middle_index = 0

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        middle_number = arr[middle_index]

        if middle_number == element_to_find:
            return middle_index

        elif middle_number < element_to_find:
            left_index = middle_index + 1

        else:
            right_index = middle_index - 1

    return -1


# tests = [[89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
#         [],
#         [1, 5, 8, 9],
#         [234, 3, 1, 56, 34, 12, 9, 12, 1300],
#         [5]]

arr1 = [12, 15, 17, 19, 21, 24, 45, 67]

print(binary_search(arr1, 17))

# for test in tests:
#     binary_search(test, 3)
#     print(test)
