# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 17:08:54 2023

@author: evere
"""

import matplotlib.pyplot as plt

S = [0, 1, 4.5, 15, 120] #0 removed for inverse graph
R = [0, 50, 81.81, 93.75, 99.17] #0 removed for inverse graph

def Recovery(x):
    return (1 - (1/(1+x)))*100

def RoundToNDigits(num, n=3):
    formatstr = '%.'+str(n)+'g'
    return float(formatstr % num)

x =[]
xInv = []
y =[]
yInv = []
for i in range(0,120):
    x.append(i)
    #xInv.append(1/i)
    y.append(Recovery(i))
    #yInv.append(1/y[-1])
for i in range(len(S)):
    plt.text(S[i], R[i], '({}, {})'.format(S[i],R[i]))
plt.plot(x,y)
plt.xlabel("Stripping Factor")
plt.ylabel("Percent Recovery")
plt.title("CHE 200 Assignment 2 \n Question 3 Graph 1")