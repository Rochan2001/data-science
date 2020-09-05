# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 08:57:05 2019

@author: rochan
"""

wordstring="it was the best of times it was the worst of times"
wordstring+="it was the age of wisdom it was the age of foolishness"
words=wordstring.split()
wordfreq=[words.count(p) for p in words]
freqdict=dict(zip(words,wordfreq))
aux=[(key,freqdict[key])for key in freqdict]
aux.sort()
print(aux)
aux.reverse()
print(aux)