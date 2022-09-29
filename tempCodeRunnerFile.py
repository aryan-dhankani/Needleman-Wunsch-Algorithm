for i in range(1 , nx+1):
        for j in range(1 , ny+1):
            if x[i-1] == y[j-1]:
                F[i][j]= max(F[i-1][j]-gap , F[i][j-1]-gap , F[i-1][j-1]+ match)
            else :
                F[i][j]= max(F[i-1][j]-gap , F[i][j-1]-gap , F[i-1][j-1]- mismatch)