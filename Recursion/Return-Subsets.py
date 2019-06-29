#!/usr/bin/env python
# coding: utf-8

# ### Problem Statement
# 
# 
# Given an integer array, find and return all the subsets of the array.
# The order of subsets in the output array is not important. However the order of elements in a particular subset should remain the same as in the input array.
# 
# *Note: An empty set will be represented by an empty list*
# 
# **Example 1**
# 
# ```
# arr = [9]
# 
# output = [[]
#           [9]]
# ```
# 
# **Example 2**
# 
# ```
# arr = [9, 12, 15]
# 
# output =  [[],
#            [15],
#            [12],
#            [12, 15],
#            [9],
#            [9, 15],
#            [9, 12],
#            [9, 12, 15]]
# ```

# In[4]:


def subsets(arr):
    """
    :param: arr - input integer array
    Return - list of lists (two dimensional array) where each list represents a subset
    TODO: complete this method to return subsets of an array
    """
    return subsets_index(arr,0)

def subsets_index(arr,index):
    if index >= len(arr):
        return [[]]
    
    temp = subsets_index(arr,index+1)
    out = list()
    for ele in temp:
        out.append(ele)
        
    for ele in temp:
        cur = list()
        cur.append(arr[index])
        cur.extend(ele)
        out.append(cur)
    return out


# <span class="graffiti-highlight graffiti-id_u30cq9y-id_2p8ft48"><i></i><button>Show Solution</button></span>

# In[5]:


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = subsets(arr)
        
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")    


# In[6]:


arr = [9]
solution = [[], [9]]

test_case = [arr, solution]
test_function(test_case)


# In[7]:


arr = [5, 7]
solution = [[], [7], [5], [5, 7]]
test_case = [arr, solution]
test_function(test_case)


# In[8]:


arr = [9, 12, 15]
solution = [[], [15], [12], [12, 15], [9], [9, 15], [9, 12], [9, 12, 15]]

test_case = [arr, solution]
test_function(test_case)


# In[9]:


arr = [9, 8, 9, 8]
solution = [[],
[8],
[9],
[9, 8],
[8],
[8, 8],
[8, 9],
[8, 9, 8],
[9],
[9, 8],
[9, 9],
[9, 9, 8],
[9, 8],
[9, 8, 8],
[9, 8, 9],
[9, 8, 9, 8]]

test_case = [arr, solution]
test_function(test_case)


# In[ ]:




