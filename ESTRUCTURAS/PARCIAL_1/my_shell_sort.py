
def my_shell_sort(arr):
    size = len(arr)
    gap = size // 2

    while gap > 0:
        # mantain the gap within comparisons
        # when looking back at elements behind
        # we always do so maintaining the gap
        
        for i in range(gap, size):
            anchor = arr[i]  # element in array we compare with elements behind it
            j = i  # index for elements behind anchor

            # if j is less than gap, j-gap will be negative (not valid)
            # arr[j-gap] > anchor compare that element behind anchor is greater than anchor
            while j >= gap and arr[j-gap] > anchor:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = anchor  # finally swap anchor element to the last remembered index
        gap = gap // 2  # divide (reduce) gap by two


tests = [[89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [5]]

arr1 = [9, 8, 3, 7, 5, 6, 4, 1]
my_shell_sort(arr1)

for test in tests:
    my_shell_sort(test)
    print(test)
