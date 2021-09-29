import numpy
numpy.set_printoptions(legacy='1.13')
X=input().split(" ")
for i in range(0,len(X)):
    X[i]=float(X[i])
my_array = numpy.array(X)
print(numpy.floor(my_array))
print(numpy.ceil(my_array))
print(numpy.rint(my_array))

