# Implements algorithms to solve a guessing game by making and evaluating guesses against potential solutions.
import numpy as np
from itertools import product


# This function compares two sequences 'x' and 'y' and returns the number of exact matches ('red')
# and the number of correct items in wrong positions ('yellow').
def compare(x, y):
    x = np.array(x)
    y = np.array(y)
    red = np.sum(x == y)
    yellow = 0
    for i in range(6):
        yellow += min(np.count_nonzero(x == i), np.count_nonzero(y == i))
    return red, yellow - red


# This function removes solutions from the list of possible solutions based on the number of red ('r')
# and yellow ('y') pegs obtained from a guess compared to the answer.
def remove_solutions(guess, r, y, solutions):
    i = 0
    while i != len(solutions):
        if compare(solutions[i], guess) != (r, y):
            del solutions[i]
            i -= 1
        i += 1
    return solutions


# This function evaluates the score (maximum occurrences of a combination of red and yellow pegs)
# for a specific guess against the remaining solutions.
def knuth_score(guess, solutions):
    pegs = np.zeros([5, 5])
    for solution in solutions:
        pegs[compare(guess, solution)] += 1
    return np.max(pegs)


# This function evaluates a score based on the sum of cubes of the occurrences of combinations
# of red and yellow pegs for a specific guess against the remaining solutions.
def my_alg_score(guess, solutions):
    pegs = np.zeros([5, 5])
    for solution in solutions:
        pegs[compare(guess, solution)] += 1
    return np.sum(np.power(pegs, 3))


# This function finds the next guess based on the provided algorithm (either 'knuth_score' or 'my_alg_score').
def find_next_guess(remaining_solutions, algorithm):
    solutions = list(product(range(6), repeat=4))
    score = np.zeros(1296)
    for i, guess in enumerate(solutions):
        score[i] = algorithm(guess, remaining_solutions)
    min_value = np.min(score)
    indexes = np.where(min_value == score)[0]
    for i in indexes:
        if solutions[i] in remaining_solutions:
            return solutions[i]
    return solutions[indexes[0]]


# This function solves the game by generating guesses and evaluating them against the answer
# until a correct guess is obtained or until the maximum number of guesses is reached.
def solve(answer, algorithm):
    remaining_solutions = list(product(range(6), repeat=4))
    initial_guess = [0, 0, 1, 1]
    if algorithm == my_alg_score:
        initial_guess = [0, 0, 1, 2]
    guesses = list()
    guesses.append(initial_guess)
    r, y = compare(initial_guess, answer)
    pegs = list()
    pegs.append((r, y))
    if r == 4:
        return guesses, pegs
    remaining_solutions = remove_solutions(initial_guess, r, y, remaining_solutions)
    for _ in range(5):
        next_guess = find_next_guess(remaining_solutions, algorithm)
        r, y = compare(next_guess, answer)
        pegs.append((r, y))
        guesses.append(next_guess)
        if r == 4:
            break
        remaining_solutions = remove_solutions(next_guess, r, y, remaining_solutions)
    return guesses, pegs
