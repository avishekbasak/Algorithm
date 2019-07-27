def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    #at least two numbers are required for determining the problem
    if not input_list or len(input_list) < 2:
        return None
    #if least consist of two numbers then return array as it is
    elif len(input_list) == 2:
        return input_list
    #otherwise sort array in descending order using merge sort which gurantees a time complexity of O(nlog n)
    sorted_list = mergesort(input_list)
    num1=0
    num2=0
    #create two largest number using alternate numbers
    for index,num in enumerate(sorted_list):
        if index%2 == 0:
            num1 = num1*10 + num
        else:
            num2 = num2*10 + num
    return [num1,num2]


def mergesort(input_list):
    if len(input_list) <= 1:
        return input_list
    #find the pivot to split the array
    mid = len(input_list) // 2
    left = input_list[:mid]
    right = input_list[mid:]
    #sort the left array and right array
    left = mergesort(left)
    right = mergesort(right)

    return merge(left,right)

def merge(left, right):

    merged = []
    left_index = 0
    right_index = 0

    #compare left array and right array, and whichever has the highest number will be inserted in the array
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
#Pass
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
#Pass
test_case = [[4, 6], [6, 4]]
test_function(test_case)
#Pass
test_case = [[4, 6,2], [64, 2]]
test_function(test_case)
#Pass
print(rearrange_digits([1]))
#None
output=rearrange_digits(None)
print(output)
#None
