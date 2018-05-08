#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interesting problem in computational combinatorics and number theory.
Problem: 
Solution by A. J. Alvarez-Socorro as a part of the Library  
Thinking_in_Algorithms
"""

# We take the function defined in the previous problem:
def is_palindrome(m):
    k=len(str(m))
    n=str(m)
    for i in range(int(k/2)):
        bolval=n[i]==n[k-1-i]
        if bolval==False:
            return False
    return True

def main():        
    maxi=0
    ii=0
    jj=0
    for i in range(9999,999,-1):
        for j in range(i,999,-1):
            if is_palindrome(i*j)==True:
                if maxi<i*j:
                    maxi=i*j
                    ii=i
                    jj=j
                    break
    return maxi,ii,jj

# Test: 
maxi, ii, jj=main()
print('The answer is:', ii, 'x', jj, '=', maxi)

            
            
