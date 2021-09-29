M=int(input())
A=[]
g=input().split(" ")
for i in range(0,M):
    A.append(int(g[i]))
N=int(input())
B=[]
g=input().split(" ")
for i in range(0,N):
    B.append(int(g[i]))
X=set(A)
Y=set(B)
Z=X.union(Y)
W=X.intersection(Y)
C=Z.difference(W)
D=list(C)
D.sort()
for i in D:
    print(i)
