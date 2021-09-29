X=set(input().split(" "))
N=int(input())
j=0
for i in range(0,N):
    B=set(input().split(" "))
    if(X.issuperset(B)):
        j+=1
        pass
    else:
        break
if(j==N):
    print('True')
else:
    print('False')
