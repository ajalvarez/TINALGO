#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interesting problem in computational combinatorics and number theory.
Problem: Given a number M, calculate the sum of all the multiples of k and n 
smaller than M. 
Solution: A. J. Alvarez-Socorro
"""

def multiples_of_n_smaller_than_m(n,m):
    L=set([])
    aux=1
    s=n
    while s<m:
        L.add(s)
        s=aux*n
        aux=aux+1
    return L

def sum_multiples_of_k_or_n_smaller_than_m(k,n,m):
    SET1=multiples_of_n_smaller_than_m(k,m)
    SET2=multiples_of_n_smaller_than_m(n,m)
    SETF=SET1.union(SET2)
    return sum(SETF)
             
    
# Test

print(sum_multiples_of_k_or_n_smaller_than_m(11,18,26))        
# 11+22+18=51