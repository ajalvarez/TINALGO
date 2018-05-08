#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interesting problem in computational combinatorics and number theory.
Problem: Write an algorithm to verify if a number is palindrome.
Solution by A. J. Alvarez-Socorro as a part of the Library  
Thinking_in_Algorithms
"""


def is_palindrome(m):
    k=len(str(m))
    n=str(m)
    for i in range(int(k/2)):
        bolval=n[i]==n[k-1-i]
        if bolval==False:
            return False
    return True

# Test 
print(is_palindrome(1234554321))
print(is_palindrome(1234584723))
