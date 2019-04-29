# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:03:49 2019

@author: s525189
"""

import matplotlib.pyplot as plt
import numpy as np
X=[]
Y= []
h=[]
S_temp=[]
S=[]


def helper(expr, first, last):
    values = []
    if((first-last)<=0.5):
        diff = 0.01
    else:
        diff = 0.05
    xvals = np.arange(first, last, diff) # Grid of 0.01 spacing from -2 to 10
    #print(xvals)
    for j in xvals:
        values.append(eval(expr.replace('x',str(j))))
    return xvals,values



spline = int(input("Enter 1 for natural spline or 2 for clamped spline"))

f = open("Values.txt", "r")
n = 0
for x in f:
  y = x.split(' ')
  X.append(int(y[0]))
  Y.append(int(y[1]))
  n = n+1
if(spline == 1):
    #Take matrix size as input
    for i in range(n-1):
        h.append(X[i+1] - X[i])
    #initialise nxn matrix with zeroes
    mat=np.zeros((n,n))
    mat[0][0] =1
    mat[n-1][n-1] =1
    #input each row at a time,with each element separated by a space
    for i in range(1,n-1):
        mat[i][i-1] = h[i-1]
        mat[i][i] = 2*(h[i-1] + h[i])
        mat[i][i+1] = h[i]
    c = np.zeros((n,1))
    for i in range(1,n-1):
        c[i] = 3*(((Y[i+1] - Y[i])/(h[i])) - ((Y[i]-Y[i-1])/h[i-1]))
    print(mat)
    mat_cpy = np.matrix(mat)
    inv_mat = mat_cpy.I
    c = (inv_mat.dot(c))
    
    b = [(((Y[i+1]-Y[i])/h[i]) - ((2*c[i]+c[i+1])*h[i]/3)) for i in range(n-1)]
    d = [(c[i+1]-c[i])/(3*h[i]) for i in range(n-1)]
    for i in range(n-1):
        z = str(Y[i])+"+"+str(b[i][0].item(0))+"*(x-"+str(X[i])+")"+"+"+str(c[i][0].item(0))+"*(x-"+str(X[i])+")**2"+"+"+str(d[i][0].item(0))+"*(x-"+str(X[i])+")**3"
        print("S(",i,"X) = ",z)
        X_val,S_temp = helper(z, X[i], X[i+1])
        plt.scatter(x=X_val, y=S_temp, marker="o")
        #print("S",i,"(X) = ", Y[i],"+",b[i][0].item(0),"*(x-",X[i],")","+",c[i][0].item(0),"*(x-",X[i],")**2","+",d[i][0].item(0),"*(x-",X[i],")**3", "for ",X[i],"<=x<",X[i+1])
        #print(eval((z)))
        print()

else:
    for i in range(n-1):
        h.append(X[i+1] - X[i])
    alph = float(input("Enter the value for alpha "))
    bet = float(input("Enter the value for beta "))

    #initialise nxn matrix with zeroes
    mat=np.zeros((n,n))
    mat[0][0] =2*h[0]
    mat[0][1]=h[0]
    mat[n-1][n-1] =2*h[n-2]
    mat[n-1][n-2] = h[n-2]
    
    #input each row at a time,with each element separated by a space
    for i in range(1,n-1):
        mat[i][i-1] = h[i-1]
        mat[i][i] = 2*(h[i-1] + h[i])
        mat[i][i+1] = h[i]
    c = np.zeros((n,1))
    c[0] = 3*(((Y[1]-Y[0])/h[0]) - alph)
    c[n-1] = 3*(bet-((Y[n-1]-Y[n-2])/h[n-2]))
    for i in range(1,n-1):
        c[i] = 3*(((Y[i+1] - Y[i])/(h[i])) - ((Y[i]-Y[i-1])/h[i-1]))
    print(mat)
    mat_cpy = np.matrix(mat)
    inv_mat = mat_cpy.I
    c = (inv_mat.dot(c))
    
    b = [(((Y[i+1]-Y[i])/h[i]) - ((2*c[i]+c[i+1])*h[i]/3)) for i in range(n-1)]
    d = [(c[i+1]-c[i])/(3*h[i]) for i in range(n-1)]
    for i in range(n-1):
        z = str(Y[i])+"+"+str(b[i][0].item(0))+"*(x-"+str(X[i])+")"+"+"+str(c[i][0].item(0))+"*(x-"+str(X[i])+")**2"+"+"+str(d[i][0].item(0))+"*(x-"+str(X[i])+")**3"
        print("S(",i,"X) = ",z)
        X_val,S_temp = helper(z, X[i], X[i+1])
        plt.scatter(x=X_val, y=S_temp, marker="o")
        #print("S",i,"(X) = ", Y[i],"+",b[i][0].item(0),"*(x-",X[i],")","+",c[i][0].item(0),"*(x-",X[i],")**2","+",d[i][0].item(0),"*(x-",X[i],")**3", "for ",X[i],"<=x<",X[i+1])
        #print(eval((z)))
        print()

plt.show()



        
        


        
        
        



