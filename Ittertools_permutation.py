X=input().split()
from itertools import permutations
Y=permutations(X[0],int(X[1]))
E=[]
for i in list(Y):
    D='' 
    for j in range(0,int(X[1])):
        D=D+i[j]
    E.append(D)
E.sort()
for i in list(E):
    print(i)

