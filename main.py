import os                                           
import sys                   
import numpy as np                       


if (os.path.exists("input.txt") == False):
    print("Input File not Found.")
    sys.exit(0)
else:
    inputFile = open("input.txt", "r")              
    
       
    xr = inputFile.readline()                    
    
    yr = inputFile.readline()
    
    xr = ''.join(xr.split())                  
    
    yr = ''.join(yr.split())

    inputFile.close() 
    
    x = list(xr)
    y = list(yr)
    
    print(y)
    
    
    gap = 2
    match = 1
    mismatch = 1
    
    nx = len(x)
    ny = len(y)
    print(nx , ny)
    
    #creating the matrix
    F = np.zeros((nx + 1 , ny + 1))
    print(F)
    
    #Filling the first row and column
    for i in range(len(x)):
        F[i+1][0] = F[i][0] - gap

    for j in range(len(y)):
        F[0][j+1] = F[0][j] - gap        
    
    print(F)
    # Directions to trace through an optimal aligment.
    P = np.zeros((nx + 1, ny + 1))
    P[:,0] = 3
    P[0,:] = 4
    # Temporary scores.
    t = np.zeros(3)
    print(t)
    for i in range(1 , nx+1):
        for j in range(1 , ny+1):
            if x[i-1] == y[j-1]:
                F[i][j]= max(F[i-1][j]-gap , F[i][j-1]-gap , F[i-1][j-1]+ match)
            else :
                F[i][j]= max(F[i-1][j]-gap , F[i][j-1]-gap , F[i-1][j-1]- mismatch)

    print(F)        
    
    i = nx
    j = ny
    x1 = '' 
    y1 = '' 
    
    while(i != 0 and j != 0) :
        if(F[i][j] == F[i-1][j]-gap) :
            x1 += x[i-1]
            y1 += '-'
            i = i-1
        elif(F[i][j] == F[i][j-1]-gap):
            y1 += y[j-1]
            x1 += '-'
            j = j-1
        else :
            y1 += y[j-1]
            x1 += x[i-1]
            i = i-1
            j = j-1
        
    
    x1 = ''.join(x1)[::-1]
    y1 = ''.join(y1)[::-1]
    
            
    print(x1)
    print(y1)