#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 09:22:10 2020

@author: ninabhatia
"""

import numpy as np
from utils import *
# %% 
'''
Implemention of Newton-CG from scratch for the Rosenbrock function
'''
func = lambda x, y: 100*(y-x**2)**2 + (1-x)**2
plot_coutour(func, box = (-2,2), scale='log');
# %%


def hessian_f(x):
    Hess = [(0,111/4), (111/4, 0)]
    return Hess




def conGrad (f, x0, grad):
    tol = 1e-6
    eta = 1e-1 # alpha in the outer loop
    N = 1000 # outer iteration 
    M = 10 # inner iteration CG
    x = np.zeros((N+1,2))
    x[0] = x0 # initial guess
    f_vals = np.zeros(N+1)
    f_vals[0] = func(x[0,0], x[0,1]) #x[0,0] is x0's x, x[0,1] is x0's y
    # %% Newton-CG
    for k in range(N): # outer iteration
        z = np.array([0.,0.])
        r = grad
        d = -r
        B = hessian_f(x[k])
        for j in range(M): # inner iteration
            if (B@d)@d <= 0: 
                '''
                check if Hessian is negative at any direction in the current search space
                '''
                if j == 0:
                    p = grad
                else:
                    '''
                    z is inner loop's search directions
                    we update the overall search direction up to the previous inner iteration where
                    the negative Hessian is obtained
                    '''
                    p = z
                '''
                jump out from the inner iteration and use -grad as the search direction
                '''
                break 
    
            '''
            the following resembles the regular CG
            '''
            alpha = r@r/((B@d)@d)
            z += alpha*d
            r_old = r
            r += alpha*(B@d)
            if np.linalg.norm(r) < tol: 
                '''
                stopping criterion of the inner iteration
                '''
                p = z
                break
            d = -r + r@r/(r_old@r_old)*d
        '''
        here p=z update the search direction if the stopping criterion of the inner iteration
        is not met and a maximum M iterations in the inner loops have been executed
        '''
        p = z
        x[k+1] = x[k] + eta*p
        f_vals[k+1] = func(x[k+1,0], x[k+1,1]) # update the function values
        m = min (fav_vals) 
        xm = np.argmin(f_vals)
        return m, xm 

def main (): 
    congrad((1.5−x+xy)**2 +􏰍 (2.25−x+xy**2􏰎)**2 +􏰍(2.625−x+xy**3)**2), [-2,-2],('gradient of beale'))
    
if __name__ == "__main__":
    main()
