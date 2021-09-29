n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(0,N):
    X=input().split(" ")
    if(X[0]=='pop'):
        s.pop()
    elif(X[0]=='remove'):
        s.remove(int(X[1]))
    elif(X[0]=='discard'):
        s.discard(int(X[1]))
su=0
for i in s:
    su+=i
print(su)
