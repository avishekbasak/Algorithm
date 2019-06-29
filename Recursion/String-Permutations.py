#!/usr/bin/env python
# coding: utf-8

# ### Problem Statement
# 
# Given an input string, return all permutations of the string in an array.
# 
# **Example 1:**
# * `string = 'ab'`
# * `output = ['ab', 'ba']`
# 
# **Example 2:**
# * `string = 'abc'`
# * `output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']`
# 

# In[36]:


def permutations(string):
    """
    :param: input string
    Return - list of all permutations of the input string
    TODO: complete this function to return a list of all permutations of the string
    """
    return permute(string,0)

def permute(string,index):
    if index >= len(string):
        return [""]
    sub_result = permute(string,index+1)
    result=list()
    char = string[index]
    for p in sub_result:
        for j in range(len(p)+1):
            new_str = p[0:j]+char+p[j:]
            result.append(new_str)
    return result
    
    


# <span class="graffiti-highlight graffiti-id_2d0q2u5-id_vkbq25t"><i></i><button>Show Solution</button></span>

# In[37]:


def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)
    print(output)
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")


# In[38]:


string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
test_function(test_case)


# In[39]:


string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [string, output]
test_function(test_case)


# In[40]:


string = 'abcd'
output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
test_case = [string, output]
test_function(test_case)


# In[ ]:




