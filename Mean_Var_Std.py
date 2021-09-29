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

print(numpy.mean(my_array, axis = 1))        #Output : [ 1.5  3.5]
print(numpy.var(my_array, axis = 0))         #Output : [ 1.  1.]
print(round(numpy.std(my_array, axis = None),11))      #Output : 1.11803398875

