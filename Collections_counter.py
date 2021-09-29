N=int(input())
Ar=input()
Arr=Ar.split(" ")
#print(Arr)
n=int(input())
Sum=0
for i in range(0,n):
    String=input()
    X=String.split(" ")
    if(X[0] in Arr):
       # print(X[0])
        Sum+=int(X[1])
        Arr.remove(X[0])
print(Sum)

