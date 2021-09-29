X=input().split()
from itertools import combinations_with_replacement
Y=combinations_with_replacement(X[0],int(X[1]))
E=[]
for i in list(Y):
    D='' 
    for j in range(0,int(X[1])):
          D=D+i[j]
    res = ''.join(sorted(D))
    E.append(res)
     
f=list(E)
f.sort()
for i in f:
    print(i)
    
