from numpy import random
import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import itertools
from itertools import combinations_with_replacement
from itertools import product
import math
import random
from itertools import permutations
A = np.array([3 , 1 , 2 , 2])
B = np.array([1, 1, 2, 3])

# solutions 
def compare(x,y):
    red = np.sum(x==y)
    yellow = 0
    for i in range(6):
        yellow += min(np.count_nonzero(x==i),np.count_nonzero(y==i))
    return red, yellow-red

def remove_solutions(guess,r,y,solutions):
    while (i != len(solutions)):
        if (compare(solutions, guess)!=r,y):
            del solutions[i]
            i-=1
        i+=1
    return solutions

def find_next_guess(solutions):
    solutions = list(product(range(6), repeat=4))
    for 

def solveKnuth(answer):
    remaining_solutions = list(product(range(6), repeat=4))
    initial_guess = [0,0,1,1]
    guesses = list().append(initial_guess)
    r,y = compare(initial_guess,answer)
    pegs = list().append((r,y))
    if r == 4:
        return guesses, pegs
    remaining_solutions = remove_solutions(initial_guess,r,y,remaining_solutions)
    while True:


# def Knuth(combination):


# def knuth_solve(row):
# print(A == B)
# print(np.where(A==B,A,10))
# print(A[A==B]==10)

# a = np.array([[0, 1, 2],
#               [0, 2, 4],
#               [0, 3, 6]])
# np.where(a < 4, a, -1)  # -1 is broadcast
# array([[ 0,  1,  2],
#        [ 0,  2, -1],
#        [ 0,  3, -1]])

# print(compare(A,B))

thislist = ["apple", "banana", "cherry", "apple", "banana", "cherry"]
for i,elem in enumerate(thislist):
    print(elem)
    print(thislist)
    thislist.pop(1)
thislist.pop()
print(thislist)


all_permutations = product(range(6), repeat=4)

# Convert permutations generator to a list to display or iterate through
all_permutations_list = list(all_permutations)

# Display the permutations
print(len(all_permutations_list))