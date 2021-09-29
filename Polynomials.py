import numpy
 
lst1 = [float(item) for item in input().split()] 
n = int(input()) 
print(numpy.polyval(lst1, n))   #Output : 34
