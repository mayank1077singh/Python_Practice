import numpy
N=int(input())
A=[]
B=[]
for i in range(0,N):
    g=input().split(" ")
    for j in range(0,N):
        g[j]=int(g[j])
    A.append(g)
for i in range(0,N):
    g=input().split(" ")
    for j in range(0,N):
        g[j]=int(g[j])
    B.append(g)
print(numpy.dot(A, B))

