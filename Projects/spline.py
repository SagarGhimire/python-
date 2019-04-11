# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:03:49 2019

@author: s525189
"""

spline = int(input("Enter 1 for natural spline or 2 for clamped spline"))
if(spline == 1):
    #Take matrix size as input
    n=int(input("Enter the number of (x,y) you want to enter "))
    X=[]
    Y= []
    h=[]
    temp = []
    X_in = 0
    Y_in = 0
    
    for i in range(n):
        X_in =int(input("Enter the value for X"))
        Y_in = int(input("Enter the value for Y"))
        X.append(X_in)
        Y.append(Y_in)
    for i in range(n-1):
        h.append(X[i+1] - X[i])
    print(h)
    import numpy as np
    
    #initialise nxn matrix with zeroes
    mat=np.zeros((n,n))
    mat[0][0] =1
    mat[n-1][n-1] =1
    #input each row at a time,with each element separated by a space
    for i in range(1,n-1):
        for j in range(i-1,i+2):
            temp.append(j)
        mat[i][temp[0]] = h[i-1]
        mat[i][temp[1]] = 2*(h[i-1] + h[i])
        mat[i][temp[2]] = h[i]
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
        print("S",i,"(X) = ", Y[i],"+",b[i],"(x-",X[i],")","+",c[i],"(x-",X[i],") ^2","+",d[i],"(x-",X[i],")^3", "for ",X[i],"<=x<",X[i+1])
else:
    n=int(input("Enter the number of (x,y) you want to enter "))
    X=[]
    Y= []
    h=[]
    temp = []
    X_in = 0
    Y_in = 0
    
    for i in range(n):
        X_in =int(input("Enter the value for X"))
        Y_in = int(input("Enter the value for Y"))
        X.append(X_in)
        Y.append(Y_in)
    for i in range(n-1):
        h.append(X[i+1] - X[i])
    alph = float(input("Enter the value for alpha"))
    bet = float(input("Enter the value for beta"))
    import numpy as np
    
    #initialise nxn matrix with zeroes
    mat=np.zeros((n,n))
    mat[0][0] =2*h[0]
    mat[0][1]=h[0]
    mat[n-1][n-1] =2*h[n-2]
    mat[n-1][n-2] = h[n-2]
    
    #input each row at a time,with each element separated by a space
    for i in range(1,n-1):
        for j in range(i-1,i+2):
            temp.append(j)
        mat[i][temp[0]] = h[i-1]
        mat[i][temp[1]] = 2*(h[i-1] + h[i])
        mat[i][temp[2]] = h[i]
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
        print("S",i,"(X) = ", Y[i],"+",b[i],"(x-",X[i],")","+",c[i],"(x-",X[i],") ^2","+",d[i],"(x-",X[i],")^3", "for ",X[i],"<=x<",X[i+1])




