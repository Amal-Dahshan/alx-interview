#!/usr/bin/python3

"""
    Module for a python program that computes the
    binomial coefficients of the pascal's triangle
    and returns the result as a list of lists
"""


def pascal_triangle(n):
    """
        A function that returns a list of lists of integers
        representing Pascal’s triangle of n
        Returns an empty list if n <= 0 that receives a parameter n
    """
    final_array = []
    compute_array = [0]

    for i in range(n):
        temp_array = []
        for j in range(i+1):
            temp_array.append(binomial_coefficient(compute_array, i, j))
        final_array.append(temp_array)
    return final_array


def binomial_coefficient(compute_array, i, j):
    """
        A function named binomial_coeffiecient that accepts parameters:
        compute_array: which stores value of the previous sequence
        i: used as numerator to form the next sequence
        j: used as a denominator in forming the next sequence
        returns a binomial sequence
    """

    if i == j or j == 0:
        compute_array[0] = 1
        return compute_array[0]
    else:
        compute_array[0] = compute_array[0] * ((i - j) + 1) // j
    return compute_array[0]
