N=int(input())
for i in range(0,N):
    n=int(input())
    X=set(input().split(" "))
    m=int(input())
    Y=set(input().split(" "))
    print(X.issubset(Y))
