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
    x=np.array(x)
    y=np.array(y)
    red = np.sum(x==y)
    yellow = 0
    for i in range(6):
        yellow += min(np.count_nonzero(x==i),np.count_nonzero(y==i))
    return red, yellow-red

def knuth_score(guess, solutions):
    pegs = np.zeros([5,5])
    for solution in solutions:
        # print(compare(guess,solution))
        pegs[compare(guess,solution)] += 1
    # print(np.max(pegs))
    # print(pegs)
    # print(np.max(pegs))
    return np.max(pegs)


def remove_solutions(guess,r,y,solutions):
    i = 0
    while (i != len(solutions)):
        # print(compare(solutions[i], guess))
        if (compare(solutions[i], guess)!=(r,y)):
            del solutions[i]
            i-=1
        i+=1
    return solutions

def find_next_guess(remaining_solutions):
    solutions = list(product(range(6), repeat=4))
    score = np.zeros(1296)

    for i,guess in enumerate(solutions):
        # print(guess)
        # print(knuth_score(guess,remaining_solutions))
        # print(remaining_solutions)
        score[i] = knuth_score(guess,remaining_solutions)
        # print(temp)


# Find the minimum value in the array
    min_value = np.min(score)
# Get indices of all occurrences of the minimum value
    indexes = np.where(min_value == score)[0]
    for i in indexes:
        if solutions[i] in remaining_solutions:
            return solutions[i]
    
    return solutions[indexes[0]]


def solveKnuth(answer):
    remaining_solutions = list(product(range(6), repeat=4))
    initial_guess = [0,0,1,1]
    guesses = list()
    guesses.append(initial_guess)
    r,y = compare(initial_guess,answer)
    pegs = list()
    pegs.append((r,y))
    if r == 4:
        return guesses, pegs
    remaining_solutions = remove_solutions(initial_guess,r,y,remaining_solutions)
    for _ in range(5):
        next_guess = find_next_guess(remaining_solutions)
        r,y = compare(next_guess,answer)
        pegs.append((r,y))
        guesses.append(next_guess)
        if r == 4:
            print(r)
            break
        remaining_solutions = remove_solutions(next_guess,r,y,remaining_solutions)
        print("len" + str(len(remaining_solutions)))
        print(r,y)
        print(next_guess)
    return guesses, pegs

# np.count_nonzero([0,0,0,0]==0)
# A, B = solveKnuth([1,2,3,4])
# print(A)
# print(B)
# def Knuth(combination):
# arr = np.array([4, 2, 1, 3, 1, 5, 1])

# # Find the minimum value in the array
# min_value = np.min(arr)

# # Get indices of all occurrences of the minimum value
# indices = np.where(arr == min_value)[0]
# print(indices)

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

# thislist = ["apple", "banana", "cherry", "apple", "banana", "cherry"]
# for i,elem in enumerate(thislist):
#     print(elem)
#     print(thislist)
#     thislist.pop(1)
# thislist.pop()
# print(thislist)


# all_permutations = product(range(6), repeat=4)

# # Convert permutations generator to a list to display or iterate through
# all_permutations_list = list(all_permutations)

# # Display the permutations
# print(len(all_permutations_list))