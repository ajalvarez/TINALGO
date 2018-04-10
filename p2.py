#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interesting problem in computational combinatorics and number theory.
Calculate the sum of all the odd Fibonacci numbers smaller than N.
Calculate the sum of all the even Fibonacci numbers smaller than N.

Solution by A. J. Alvarez-Socorro as a part of the Library  
Thinking_in_Algorithms
"""

def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fibonacci_numbers_smaller_than(n):
    aux=2
    newf=1
    L=[]
    while newf<n:
        L.append(newf)
        newf=fib(aux)
        aux=aux+1
    return L

def even_fibonacci_numbers_smaller_than(n):
    ALL=fibonacci_numbers_smaller_than(n)
    EVEN=[]
    for number in ALL:
        if number%2==0:
            EVEN.append(number)
    return EVEN

def odd_fibonacci_numbers_smaller_than(n):
    ALL=fibonacci_numbers_smaller_than(n)
    ODD=[]
    for number in ALL:
        if number%2==1:
            ODD.append(number)
    return ODD

def sum_even_fib(n):
    return sum(even_fibonacci_numbers_smaller_than(n))

def sum_odd_fib(n):
    return sum(odd_fibonacci_numbers_smaller_than(n))

        

# Test
# odd Fibonacci numbers smaller than 20: [1,3,5,13] and the sum is 22
print(sum_odd_fib(20))

# even Fibonacci numbers smaller than 40: [2,8,34] and the sum is 44
print(sum_even_fib(40))        