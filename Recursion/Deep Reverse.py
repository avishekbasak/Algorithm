#!/usr/bin/env python
# coding: utf-8

# ## Problem Statement
# 
# Define a procedure, `deep_reverse`, that takes as input a list, and returns a new list that is the deep reverse of the input list.  
# This means it reverses all the elements in the list, and if any of those elements are lists themselves, reverses all the elements in the inner list, all the way down. 
# 
# >Note: The procedure must not change the input list itself.
# 
# 
# 

# In[11]:


def deep_reverse(arr):
    return deep_rev(arr,0)

def deep_rev(arr,index):
    if index == len(arr):
        return list()
    
    out = deep_rev(arr,index+1)
    res=None
    if is_list(arr[index]):
        res = deep_reverse(arr[index])
    else:
        res = arr[index]
    out.append(res)
    return out

def is_list(item):
    return isinstance(item,list)


# <span class="graffiti-highlight graffiti-id_25r0ar8-id_l0hi76f"><i></i><button>Show Solution</button></span>

# In[12]:


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = deep_reverse(arr)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("False")


# In[13]:


arr = [1, 2, 3, 4, 5]
solution = [5, 4, 3, 2, 1]
test_case = [arr, solution]
test_function(test_case)


# In[14]:


arr = [1, 2, [3, 4, 5], 4, 5]
solution = [5, 4, [5, 4, 3], 2, 1]
test_case = [arr, solution]
test_function(test_case)


# In[15]:


arr = [1, [2, 3, [4, [5, 6]]]]
solution = [[[[6, 5], 4], 3, 2], 1]
test_case = [arr, solution]
test_function(test_case)


# In[16]:


arr =  [1, [2,3], 4, [5,6]]
solution = [ [6,5], 4, [3, 2], 1]
test_case = [arr, solution]
test_function(test_case)


# In[ ]:




