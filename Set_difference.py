N=int(input())
X=input().split(" ")
M=int(input())
Y=input().split(" ")
A=set(X)
B=set(Y)
print(len(A.difference(B)))

