K=int(input())
X=input().split(" ")
A=list(set(X))
A=A+A
for i in X:
    try:
        A.remove(i)
    except:
        pass
print(A[0])
