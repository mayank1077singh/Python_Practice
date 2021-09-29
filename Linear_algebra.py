import numpy
n = int(input()) 
A=[]
for i in range(0,n):
    g=input().split(" ")
    for j in range(0,n):
        g[j]=float(g[j])
    A.append(g)
print(round(numpy.linalg.det(A),2))
