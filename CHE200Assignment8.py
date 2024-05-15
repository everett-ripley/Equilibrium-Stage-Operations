# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 11:32:56 2023

@author: evere
"""
#Trapezoid rule specifically for Batch Distillation
import matplotlib.pyplot as plt
import math

F = 100
x_f = 0.3965
x_w = 0.1238

x_list =[0.0,
         0.019,
         0.0721,
         0.0966,
         0.1238,
         0.1661,
         0.2377,
         0.2608,
         0.3273,
         0.3965,
         0.5079,
         0.5198,
         0.5732,
         0.6763,
         0.7472,
         0.8943,
         1.0]
y_list =[0.0,
         0.17,
         0.3891,
         0.4375,
         0.4704,
         0.5089,
         0.5445,
         0.558,
         0.5826,
         0.6122,
         0.6564,
         0.6599,
         0.6841,
         0.7385,
         0.7815,
         0.8943,
         1.0]

#Setting bounds of integration
x_lower_bound = 0.1238
x_upper_bound = 0.3965
y_lower_bound = 0.4704
y_upper_bound = 0.6122
x_int_list = []
y_int_list = []
def set_integral_bounds(x_lower, x_upper, y_lower, y_upper, total_x, total_y):
    x_integration = []
    y_integration = []
    for i in range(len(total_x)):
        if total_x[i] >= x_lower and total_x[i] <= x_upper:
            x_integration.append(total_x[i])
        if total_y[i] >= y_lower and total_y[i] <= y_upper:
            y_integration.append(total_y[i])
    return x_integration, y_integration

x_int_list, y_int_list = set_integral_bounds(x_lower_bound, x_upper_bound, y_lower_bound, y_upper_bound, x_list, y_list)

func_list = []

def base(x_initial, x_final):
    return (x_final - x_initial)

def function(x, y):
    return 1/(y-x)

def round_to_digits(num, n=2):
    format_string = '%.'+str(n)+'g'
    return float(format_string % num)

if len(x_list) == len(y_list):
    
    #Solving
    integral_estimation = 0.0
    for i in range(len(x_int_list) -1):
        if x_int_list[i] != y_int_list[i] and x_int_list[i+1] != y_int_list[i+1]:
            integral_estimation += base(x_int_list[i], x_int_list[i+1]) * 0.5 * (function(x_int_list[i], y_int_list[i]) + function(x_int_list[i+1], y_int_list[i+1])) 
    
    remove_index = []
    for i in range(len(x_list)):
        if x_list[i] != y_list[i]:
            func_list.append(function(x_list[i], y_list[i]))
        else:
            remove_index.append(i)
    
    def sort_list_max_to_min(lst):
        new_lst = []
        for i in range(len(lst)):
            new_lst.append(max(lst))
            lst.pop(lst.index(max(lst)))
        return new_lst
    
    remove_index = sort_list_max_to_min(remove_index)
    
    for i in range(len(remove_index)):
        x_list.pop(remove_index[i])
        
    #Graphing
    plt.plot(x_list, func_list)
    
    points_list=[]
    for i in range(len(x_list)):
        points_list.append((x_list[i], func_list[i]))
        plt.text(x_list[i], func_list[i], '({}, {})'.format(round_to_digits(x_list[i]), round_to_digits(func_list[i])))
    
    plt.xlabel("Liquid mole fraction of ethanol, x")
    plt.ylabel("(y-x)^-1")
    plt.title("Full Data Set")
    plt.show()
    
    narrow_y_list = []
    for i in range(len(x_int_list)):
        if x_list[i] != y_list[i]:
            narrow_y_list.append(function(x_int_list[i], y_int_list[i]))
    plt.plot(x_int_list, narrow_y_list)
    
    for i in range(len(x_int_list)):
        plt.text(x_int_list[i], narrow_y_list[i], '({}, {})'.format(round_to_digits(x_int_list[i]), round_to_digits(narrow_y_list[i])))
    
    plt.xlabel("Liquid mole fraction of ethanol, x")
    plt.ylabel("(y-x)^-1")
    plt.title("Integration Area")
    plt.show()
    
        
    #Answer
    W = F * math.e**(-1*integral_estimation)
    D = F - W
    x_d = (x_f * F - x_w * W)/D
    W = round_to_digits(W, 3)
    D = round_to_digits(D, 3)
    x_d = round_to_digits(x_d, 3)
    print(f"Area Approximation: {integral_estimation}\nDistillate Collected: {D}\nRemaining Residue: {W}\nAverage Distillate Composition: {x_d}")
    
else:
    #Input error management
    print("Unequal Lists!")
