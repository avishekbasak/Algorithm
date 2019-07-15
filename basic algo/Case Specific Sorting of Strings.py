#!/usr/bin/env python
# coding: utf-8

# # Case Specific Sorting of Strings
# 
# ## Problem statement
# Given a string consisting of uppercase and lowercase ASCII characters, write a function, `case_sort`, that sorts uppercase and lowercase letters separately, such that if the $i$th place in the original string had an uppercase character then it should not have a lowercase character after being sorted and vice versa.
# 
# For example:  
# **Input:** fedRTSersUXJ  
# **Output:** deeJRSfrsTUX

# In[6]:


def case_sort(string):
    """
    Here are some pointers on how the function should work:
    1. Sort the string
    2. Create an empty output list
    3. Iterate over original string
        if the character is lower-case:
            pick lower-case character from sorted string to place in output list
        else:
            pick upper-case character from sorted string to place in output list
    
    Note: You can use Python's inbuilt ord() function to find the ASCII value of a character
    """
    up_chr_idx = 0
    lw_chr_idx = 0
    
    sorted_str = sorted(string)
    for idx,chr in enumerate(sorted_str):
        if 97 <= ord(chr)<=122:
            lw_chr_idx = idx
            break
    output = ''
    for ch in string:
        if 97 <=ord(ch) <=122:
            output+=sorted_str[lw_chr_idx]
            lw_chr_idx += 1
        else:
            output+=sorted_str[up_chr_idx]
            up_chr_idx += 1
    return output


# <span class="graffiti-highlight graffiti-id_mw53bf1-id_fsblbn3"><i></i><button>Show Solution</button></span>

# In[7]:


def test_function(test_case):
    test_string = test_case[0]
    solution = test_case[1]
    
    if case_sort(test_string) == solution:
        print("Pass")
    else:
        print("False")


# In[8]:


test_string = 'fedRTSersUXJ'
solution = "deeJRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)


# In[9]:


test_string = "defRTSersUXI"
solution = "deeIRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)


# In[ ]:




