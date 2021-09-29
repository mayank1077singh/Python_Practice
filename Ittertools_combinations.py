X=input().split()
from itertools import combinations
for k in range(1,int(X[1])+1):
   Y=combinations(X[0],k)
   E=[]
   g=0
   for i in list(Y):
      D='' 
      for j in range(0,k):
          D=D+i[j]
      res = ''.join(sorted(D))
      E.append(res)
     
   f=list(E)
   f.sort()
   for i in f:
      print(i)
