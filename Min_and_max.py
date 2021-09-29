import numpy
X=input().split(" ")
N=int(X[0])
M=int(X[1])
Y=[]
for i in range(0,N):
    g=input().split(" ")
    for j in range(0,M):
        g[j]=int(g[j])
    Y.append(g)
my_array = numpy.array(Y)
A=numpy.min(my_array, axis = 1)
print(numpy.max(A))

