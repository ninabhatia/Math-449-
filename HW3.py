import numpy as np


def f(x): 
    z = np.sin(3.14*x)
    return z 


def v (x_min, x_max, N): 
    x = np.linspace(x_min, x_max, N)
    l = f(x)
    return l


def pm (x_min, x_max, N): 
    I = np.diag(np.ones(N)) 
    h = ((x_max-x_min)/N)
    A = (2-h*h)*I - np.diag(np.ones(N-1), k=1) -  np.diag(np.ones(N-1), k=-1)
    
   
    tol = 1e-4
    err = tol + 1
   
    lambda_h = [] # empty list
    k = 0
   
    while err >= tol:
        y = v(x_min, x_max, N) 
        b = A@y
        
        tmp1 = b.dot(y)
        tmp2 = y.dot(y)
        b = b/np.linalg.norm(b)
        err = np.linalg.norm(y - b)
        y = b 
        lambda_h.append(tmp1/tmp2)
        k += 1
        if k > 10000:
            break

    m = max (lambda_h)
    print (m)
    return (m)


pm(0,1,21)     
     











