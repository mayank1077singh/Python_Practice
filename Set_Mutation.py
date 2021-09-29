N=int(input())
X=input().split(" ")
A= set(X)
n=int(input())
for i in range(0,n):
    g=input().split(" ")
    h=input().split(" ")
    H=set(h)
    if(g[0]=='update'):
        A.update(H)
    elif(g[0]=='intersection_update'):
        A.intersection_update(H)
    elif(g[0]=='difference_update'):
        A.difference_update(H)
    elif(g[0]=='symmetric_difference_update'):
        A.symmetric_difference_update(H)
su=0
for i in A:
  su+=int(i)
print(su)
