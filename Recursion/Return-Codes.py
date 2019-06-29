#!/usr/bin/env python
# coding: utf-8

# ### Problem statement
# 
# In an encryption system where ASCII lower case letters represent numbers in the pattern `a=1, b=2, c=3...` and so on, find out all the codes that are possible for a given input number. 
# 
# **Example 1**
# 
# * `number = 123`
# * `codes_possible = ["aw", "abc", "lc"]`
# 
# Explanation: The codes are for the following number:
#          
# * 1 . 23     = "aw"
# * 1 . 2 . 3  = "abc"
# * 12 . 3     = "lc"
#     
# 
# **Example 2**  
# 
# * `number = 145`
# * `codes_possible = ["ade", "ne"]`
# 
# Return the codes in a list. The order of codes in the list is not important.
# 
# *Note: you can assume that the input number will not contain any 0s*

# In[5]:


def all_codes(number):
    """
    :param: number - input integer
    Return - list() of all codes possible for this number
    TODO: complete this method and return a list with all possible codes for the input number
    """
    
    if number == 0:
        return [""]
    
    # calculate code for group of 2
    remainder = number % 100
    out_2 = list()
    if remainder <= 26 and number > 9 :
        out_2 = all_codes(number // 100)
        alphabet = get_Char(remainder)
        for index, element in enumerate(out_2):
            #concatenate new alphabet to the rest
            out_2[index] = element + alphabet
    
    # calculation for group of 1
    remainder = number % 10
    out_1 = all_codes(number // 10)
    alphabet = get_Char(remainder)
    
    for index, element in enumerate(out_1):
        #concatenate new alphabet to the rest
        out_1[index] = element + alphabet
        
    #append both result
    output = list()
    output.extend(out_2)
    output.extend(out_1)
    
    return output
    
    pass

def get_Char(number):
    """
    return ASCII lower case character. ascii of lower  case 'a' starts from 97
    """
    return chr(number+96)


# <span class="graffiti-highlight graffiti-id_q8i2zj9-id_yrg0ir2"><i></i><button>Show Solution</button></span>

# In[6]:


def test_function(test_case):
    number = test_case[0]
    solution = test_case[1]
    
    output = all_codes(number)
    
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")


# In[7]:


number = 123
solution = ['abc', 'aw', 'lc']
test_case = [number, solution]
test_function(test_case)


# In[8]:


number = 145
solution =  ['ade', 'ne']
test_case = [number, solution]
test_function(test_case)


# In[9]:


number = 1145
solution =  ['aade', 'ane', 'kde']
test_case = [number, solution]
test_function(test_case)


# In[10]:


number = 4545
solution = ['dede']
test_case = [number, solution]
test_function(test_case)


# In[ ]:




