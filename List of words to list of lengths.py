#!/usr/bin/env python
# coding: utf-8

# In[13]:


"""
Problem Statement 1:
Write a Python program using function concept that maps list of words into a list of
integers representing the lengths of the corresponding words.
"""
def WordsToLengths(lstWords):
    lstLengths = []
    for x in range(len(lstWords)):
        lstLengths.append(len(lstWords[x]))
    return lstLengths

def wordlength(wdlist):
    return list(map(lambda x: len(x), wdlist))

lstwrd = ['ab','cde','erty']
#print(WordsToLengths(lstwrd))

print ("word lengths in array : " + str(wordlength(lstwrd)))

