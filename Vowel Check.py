#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Problem Statement 2:
Write a Python function which takes a character (i.e. a string of length 1) and returns
True if it is a vowel, False otherwise.
"""

def vowelChk(char):
    if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
        return True
    else:
        return False

# Take user input
char = input("Enter character: ");

# If Invalid input, exit
if (len(char) > 1):
    print("string Length must be one")
    exit();
else:
    # If Invalid input, exit
    if (char.isalpha() == False):
        print("Invalid entry")
    else:
        # Invoke function
        if (vowelChk(char)):
            print(char, "is a vowel.");
        else:
            print(char, "is not a vowel."); 

