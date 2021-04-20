import numpy as np

#User Input 
a =int(input('a value: '))
n =int(input ('number of iterations: '))
x0=float(input ('initial x value: '))

#this functions returns f(x) as given in hw for a positive value 
def f(x):  
    function = x**3 - a
    return function

#this function returns the derative of f(x) 
def df(x):
    derivative = 3*(x**2)
    return derivative  

#Performs newtons method for given f(x) and f0
def newtonArray (f, df, x0, n): 
    x = np.zeros(n+1) #creates array of size n+1 filled with zeros 
    x[0]= x0 #look at first place in list x i.e. index 0 and set it to be the user inputed x0
    for k in range(n): 
        #for every integer starting with 0 and n we want to look at next place over and put in the computation of newtons method
        x[k+1] = x[k]-f(x[k])/df(x[k])
    return x 

print (newtonArray(f, df, x0, n))
