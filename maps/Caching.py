#!/usr/bin/env python
# coding: utf-8

# Caching can be defined as the process of storing data into a temporary data storage to avoid recomputation or to avoid reading the data from a relatively slower part of memory again and again. Thus cachig serves as a fast "look-up" storage allowing programs to execute faster.  
# 
# Let's use caching to chalk out an efficient solution for a problem.

# ### Problem Statement
# 
# A child is running up a staircase with and can hop either 1 step, 2 steps or 3 steps at a time. 
# If the staircase has `n` steps, write a function to count the number of possible ways in which child can run up the stairs. 
# 
# For e.g. 
# 
# * `n == 1` then `answer = 1`
# 
# * `n == 3` then `answer = 4`
#  
# * `n == 5` then `answer = 13`

# In[1]:


def staircase(n):
    # Base Case - minimum steps possible and number of ways the child can climb them

    # Inductive Hypothesis - ways to climb rest of the steps
    
    # Inductive Step - use Inductive Hypothesis to formulate a solution
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)


# In[2]:


def test_function(test_case):
    answer = staircase(test_case[0])
    if answer == test_case[1]:
        print("Pass")
    else:
        print("Fail")
            


# In[3]:


test_case = [4, 7]
test_function(test_case)


# In[4]:


test_case = [5, 13]
test_function(test_case)


# In[5]:


test_case = [3, 4]
test_function(test_case)


# In[6]:


test_case = [20, 121415]
test_function(test_case)


# <span class="graffiti-highlight graffiti-id_r189hz6-id_vtju73f"><i></i><button>Show Solution</button></span>

# ### Problem Statement
# 
# While using recursion for the above problem, you might have noticed a small problem with efficiency.
# 
# Let's take a look at an example.
# 
# * Say the total number of steps are `5`. This means that we will have to call at `(n=4), (n=3), and (n=2)`
# 
# * To calculate the answer for `n=4`, we would have to call `(n=3), (n=2) and (n=1)`
# 
# You can notice that even for a small number of staircases (here 5), we are calling `n=3` and `n=2` multiple times. Each time we call a method, additional time is required to calculate the solution. In contrast, instead of calling on a particular value of `n` again and again, we can calculate it once and store the result to speed up our program.
# 
# Your job is to use any data-structure that you have used until now to write a faster implementation of the function you wrote earlier while using recursion. 
# 

# In[8]:


def staircase(n):
    step_map=dict({})
    return staircase_count(n,step_map)

def staircase_count(n,step_map):
    if n == 1:
        res = 1
    elif n == 2:
        res = 2
    elif n == 3:
        res = 4
    else:
        if (n-1) in step_map:
            out_1 = step_map[n-1]
        else:
            out_1 = staircase_count(n-1,step_map)
        if (n-2) in step_map:
            out_2 = step_map[n-2]
        else:
            out_2 = staircase_count(n-2,step_map)
        if (n-3) in step_map:
            out_3 = step_map[n-3]
        else:
            out_3 = staircase_count(n-3,step_map)
        res = out_1+out_2+out_3
    step_map[n]=res    
    return res


# In[9]:


test_case = [4, 7]
test_function(test_case)


# In[10]:


test_case = [5, 13]
test_function(test_case)


# In[11]:


test_case = [3, 4]
test_function(test_case)


# In[12]:


test_case = [20, 121415]
test_function(test_case)


# <span class="graffiti-highlight graffiti-id_0n79ls8-id_6t02ke7"><i></i><button>Show Solution</button></span>
