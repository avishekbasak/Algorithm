#!/usr/bin/env python
# coding: utf-8

# ### Problem Statement
# 
# Given list of integers that contain numbers in random order, write a program to find the longest possible sub sequence of consecutive numbers in the array. Return this subsequence in sorted order. The solution must take O(n) time
# 
# For e.g. given the list `5, 4, 7, 10, 1, 3, 55, 2`, the output should be `1, 2, 3, 4, 5`
# 
# *Note- If two arrays are of equal length return the array whose index of smallest element comes first.*
# 
# 

# In[24]:


def longest_consecutive_subsequence(input_list):
    # TODO: Write longest consecutive subsequence solution
    ele_dict = dict()
    # iterate over the list and store element in a suitable data structure
    for idx,ele in enumerate(input_list):
        ele_dict[ele] = idx
        
    max_len = -1
    starts_at = len(input_list)
    
    for idx,ele in enumerate(input_list):
        current_start = idx
        ele_dict[ele] = -1
        
        current_count = 1
        
        current = ele+1
        
        while current in ele_dict and ele_dict[current] > 0:
            current_count += 1
            ele_dict[current] = -1
            current = current+1
            
        current = ele -1
        while current in ele_dict and ele_dict[current]>0:
            current_start = ele_dict[current]
            current_count += 1
            ele_dict[current] = -1
            current = current - 1
    
    # traverse / go over the data structure in a reasonable order to determine the solution
        if current_count >= max_len:
            if current_count == max_len and current_starts > starts_at:
                continue
            starts_at = current_start
            max_len = current_count

    start_element = input_list[starts_at]
    return [element for element in range(start_element, start_element + max_len)]


# In[25]:


def test_function(test_case):
    output = longest_consecutive_subsequence(test_case[0])
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")
    


# In[26]:


test_case_1 = [[5, 4, 7, 10, 1, 3, 55, 2], [1, 2, 3, 4, 5]]
test_function(test_case_1)


# In[27]:


test_case_2 = [[2, 12, 9, 16, 10, 5, 3, 20, 25, 11, 1, 8, 6 ], [8, 9, 10, 11, 12]]
test_function(test_case_2)


# In[28]:


test_case_3 = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
test_function(test_case_3)


# <span class="graffiti-highlight graffiti-id_et1ek54-id_r15x1vg"><i></i><button>Show Solution</button></span>
