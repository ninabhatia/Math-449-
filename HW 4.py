#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 17:06:58 2020

@author: ninabhatia
Homework 4 Code 
"""
import numpy as np
import scipy.linalg as la


def simpleOptim (A, b):
    
    print( "\nMatrix A: ")
    print (A)
    
    print ("\nVector b:")
    print (b)
    
    """min Eigenvalue calculator"""
    lambdA = np.linalg.eigvals(A)
    lmin =min(lambdA)

  
    
    if lmin>0: 
        xmin =(np.linalg.inv(((1/2)*(A+A.transpose())))).dot(b)
        fmin = (1/2)*(xmin.transpose().dot(A)).dot(xmin)-b.transpose().dot(xmin)
    
     
    elif lmin==0: #A is positive semidefinite 
        newA = A + A.transpose()
        newb = b+b
        xmin = la.solve(newA, newb)
        fmin = (1/2)*((xmin.transpose().dot(A)).dot(xmin))- ((b.transpose()).dot(xmin))
           
    else: 
        print("Matrix not valid")
        fmin = 0
        xmin = 0
        
        
    print ("\nfmin is:")
    print (fmin)
    print ("\nxmin is:")
    print (xmin)
    
    
    return( fmin, xmin)



'''
m = np.array([ [2, -2],
                 [-2,5]])
    
     
Bentries = np.array([1,2])
b = Bentries
    
ugh = simpleOptim(m,b)
print (ugh)
'''


def main (): 
    
    """"Matrix A from user input"""
    N = int(input("Enter the number of rows/columns: ")) 
    print("Enter the entries for A in a single line seperated by spaces: ")  
    Aentries = list(map(int, input().split())) 
    A = np.array(Aentries).reshape(N, N)
    
    """"Vector b from user input"""
    print("Enter the entries for b in a single line seperated by spaces: ")  
    Bentries = list(map(int, input().split())) 
    b = np.array(Bentries).reshape(N, 1)
    
    ans = simpleOptim(A, b)
    print ("\nDone!")
    
    
if __name__ == "__main__":
    main()
    
    

