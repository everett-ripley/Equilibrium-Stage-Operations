# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 16:11:40 2023

@author: evere
"""
L = 100
V = 100
K = 15
Yin = 0.0
Xin = 0.1
Title = "Test \n Graph"


import matplotlib.pyplot as plt
import numpy as np

def RoundToNDigits(num, n=3):
    formatstr = '%.'+str(n)+'g'
    return float(formatstr % num)

def HenrysLaw(x, K):
    return K * x

def OperatingLine(L, V, Yin, Xin, X):
    return Yin - (L/V) * (X - Xin)

def SolveIntersection(L, V, Yin, Xin, K):
    LVRatio = L/V
    
    X = (Yin + LVRatio * Xin)/(K + LVRatio)
    Y = K * X
    return (RoundToNDigits(X), RoundToNDigits(Y))

PoI = SolveIntersection(L, V, Yin, Xin, K)
x = np.array([PoI[0] - 0.0075, PoI[0] + 0.0075])
if x[0] < 0:
    x[0] = 0
if x[1] > 1:
    x[1] = 1
if PoI[0] > 1 or PoI[0] < 0 or PoI[1] > 1 or PoI[1] < 0:
    print("WARNING: Bad Intersection Values")
    
a = lambda x : HenrysLaw(x, K)
y = a(x)
plt.plot(x, y, label = "Henry's Law (y = kx)")
b = lambda x : OperatingLine(L, V, Yin, Xin, x)
y = b(x)
plt.text(PoI[0], PoI[1], '({}, {})'.format(PoI[0], PoI[1]))
plt.plot(x, y, label = "Operating Line (y = y_in - (L/V)(x - x_in))")
plt.legend()
plt.title(Title)
plt.xlabel("Liquid Solute Final Mole Fraction")
plt.ylabel("Gaseous Solute Final Mole Fraction")
plt.show()


