def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    if not input_list or len(input_list) == 0:
        return -1
    if len(input_list) == 1:
        if input_list[0] == number:
            return 0
        else:
            return -1

    start = 0
    end = len(input_list)-1
    mid = -1;
    while start <= end:
        mid = (start +end)//2
        if input_list[mid] == number:
            return mid
        # check if right side is sorted or left side is unsorted
        elif input_list[mid] < input_list[end] or input_list[mid] < input_list[start]:
            # check if number is greater than mid and less than end: number is in right side else left side
            if number > input_list[mid] and number <= input_list[end]:
                start = mid + 1
            else:
                end = mid - 1
        # check if left side is sorted or right side is unsorted
        elif input_list[mid] > input_list[end] or input_list[mid] > input_list[start]:
            # check if number is less than mid and greater than start: number is in left side else right side
            if number < input_list[mid] and number >= input_list[start]:
                end = mid -1
            else:
                start = mid + 1
        #if we are here that means nummber does not seem to fir in above blocks, so move start to one block ahead
        else:
            start += 1
    return -1;

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
#Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
#Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
#Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
#Pass
test_function([[6, 10, 8, 1, 2, 3, 4], 10])
#Pass
test_function([[], 10])
#Pass
test_function([[6], 6])
#Pass
test_function([[7], 6])
#Pass
print(rotated_array_search(None,6))
#-1
