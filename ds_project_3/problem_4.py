
def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    #if list is none  or of length 1 return as it is
    if not input_list or len(input_list) == 1:
        return input_list

    #have a start pointer and end pointer to track the value of 0 and 2.
    #have a index pointer to track current position
    #have a pivot around which we need to sort. Here we have pivot value as 1
    start = 0
    indx = 0
    end = len(input_list) - 1
    pivot = 1

    #iterate till the list is traversed
    while indx<=end:
        #if current index value is less than pivot, swap the start index and current index and increment both
        if input_list[indx] < pivot:
            swap(input_list,start,indx)
            start+=1
            indx+=1
        #if current index value is more than pivot, swap the end index and decremment end indx
        elif input_list[indx] > pivot:
            swap(input_list,indx,end)
            end-=1
        else:
        #if current index value is equal to pivot,move ahead
            indx+=1

    return input_list


def swap(input_list,pos1,pos2):
    '''
    this method swaps the position 1 and 2 of input_list
    '''
    input_list[pos1],input_list[pos2] = input_list[pos2],input_list[pos1]


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
#[0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
#Pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
#Pass
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
#[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
#Pass
test_function([2,2,2,0,0,0,1,1])
#[0, 0, 0, 1, 1, 2, 2, 2]
#Pass
test_function([1,1,1,0,0,0,2,2])
#[0, 0, 0, 1, 1, 2, 2, 2]
#Pass
test_function([2])
#[2]
#Pass
print(sort_012(None))
#None
