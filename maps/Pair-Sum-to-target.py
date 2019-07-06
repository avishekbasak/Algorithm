#!/usr/bin/env python
# coding: utf-8

# ### Problem statement
# 
# Given an `input_list` and a `target`, return the indices of pair of integers in the list that sum to the target. The best solution takes O(n) time. You can assume that the list does not have any duplicates.
# 
# For e.g. `input_list = [1, 5, 9, 7]` and `target = 8`, the answer would be `[0, 3]` 

# In[43]:


def pair_sum_to_zero(input_list, target):
    # TODO: Write pair sum to zero function
    num_map=dict()
    for index,num in enumerate(input_list):
        if target-num in num_map:
            return [num_map[target-num],index]
        num_map[num] = index

        
        


# In[44]:


def test_function(test_case):
    output = pair_sum_to_zero(test_case[0], test_case[1])
    print(output)
    if sorted(output) == test_case[2]:
        print("Pass")
    else:
        print("Fail")


# In[45]:


test_case_1 = [[1, 5, 9, 7], 8, [0, 3]]
test_function(test_case_1)


# In[46]:


test_case_2 = [[10, 5, 9, 8, 12, 1, 16, 6], 16, [0, 7]]
test_function(test_case_2)


# In[47]:


test_case_3 = [[0, 1, 2, 3, -4], -4, [0, 4]]
test_function(test_case_3)


# <span class="graffiti-highlight graffiti-id_snm0ke6-id_tv0tye7"><i></i><button>Show Solution</button></span>

# In[ ]:




