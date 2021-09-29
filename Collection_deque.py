from collections import deque
N=int(input())
d=deque()
s=''
for i in range(0,N):
    g=input().split(" ")
    if(g[0]=='append'):
        d.append(int(g[1]))
    elif(g[0]=='appendleft'):
        d.appendleft(int(g[1]))
    elif(g[0]=='pop'):
        d.pop()
    elif(g[0]=='popleft'):
        d.popleft()
for i in d:
    s=s+str(i)+' '
print(s)
