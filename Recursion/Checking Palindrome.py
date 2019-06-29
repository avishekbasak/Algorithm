#!/usr/bin/env python
# coding: utf-8

# # Palindrome

# A **palindrome** is a word that is the reverse of itself—that is, it is the same word when read forwards and backwards.
# 
# For example:
# *  "madam" is a palindrome
# * "abba" is a palindrome
# *  "cat" is not
# *  "a" is a trivial case of a palindrome
# 
# The goal of this exercise is to use recursion to write a function `is_palindrome` that takes a string as input and checks whether that string is a palindrome. (Note that this problem can also be solved with a non-recursive solution, but that's not the point of this exercise.)

# In[3]:


def is_palindrome(input):
    """
    Return True if input is palindrome, False otherwise.
    
    Args:
       input(str): input to be checked if it is palindrome
    """
    
    # TODO: Write your recursive palindrome checker here
    
    if len(input)<1:
        return True
    return input[0]==input[-1] and is_palindrome(input[1:-1])
        


# In[4]:


# Test Cases

print ("Pass" if  (is_palindrome("")) else "Fail")
print ("Pass" if  (is_palindrome("a")) else "Fail")
print ("Pass" if  (is_palindrome("madam")) else "Fail")
print ("Pass" if  (is_palindrome("abba")) else "Fail")
print ("Pass" if not (is_palindrome("Udacity")) else "Fail")


# <span class="graffiti-highlight graffiti-id_crohunx-id_mwh78k9"><i></i><button>Show Solution</button></span>

# In[ ]:




