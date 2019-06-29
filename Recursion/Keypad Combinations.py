#!/usr/bin/env python
# coding: utf-8

# ## Keypad Combinations
# 
# A keypad on a cellphone has alphabets for all numbers between 2 and 9. 
# 
# You can make different combinations of alphabets by pressing the numbers.
# 
# For example, if you press 23, the following combinations are possible:
# 
# `ad, ae, af, bd, be, bf, cd, ce, cf`
# 
# Note that because 2 is pressed before 3, the first letter is always an alphabet on the number 2.
# Likewise, if the user types 32, the order would be
# 
# `da, db, dc, ea, eb, ec, fa, fb, fc`
# 
# 
# Given an integer `num`, find out all the possible strings that can be made using digits of input `num`. 
# Return these strings in a list. The order of strings in the list does not matter. However, as stated earlier, the order of letters in a particular string matters.

# In[6]:


def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


def keypad(num):
    
    # TODO: Write your keypad solution here!
    
    if num <=1:
        return [""]
    elif 1 < num <=9:
        return list(get_characters(num))
    
    cur_num = num%10
    small_output = keypad(num//10)
    string = get_characters(cur_num)
    out=[]
    for ch in string:
        for i in small_output:
            new_str  = i+ch
            out.append(new_str)
    return out


# In[7]:


def test_keypad(input, expected_output):
    if sorted(keypad(input)) == expected_output:
        print("Yay. We got it right.")
    else:
        print("Oops! That was incorrect.")


# In[8]:


# Base case: list with empty string
input = 0
expected_output = [""]
test_keypad(input, expected_output)


# In[9]:


# Example case
input = 23
expected_output = sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
test_keypad(input, expected_output)


# In[10]:


# Example case
input = 32
expected_output = sorted(["da", "db", "dc", "ea", "eb", "ec", "fa", "fb", "fc"])
test_keypad(input, expected_output)


# In[11]:


# Example case
input = 8
expected_output = sorted(["t", "u", "v"])
test_keypad(input, expected_output)


# In[12]:


input = 354
expected_output = sorted(["djg", "ejg", "fjg", "dkg", "ekg", "fkg", "dlg", "elg", "flg", "djh", "ejh", "fjh", "dkh", "ekh", "fkh", "dlh", "elh", "flh", "dji", "eji", "fji", "dki", "eki", "fki", "dli", "eli", "fli"])
test_keypad(input, expected_output)


# <span class="graffiti-highlight graffiti-id_9ibtd5w-id_haj1ksk"><i></i><button>Show Solution</button></span>
