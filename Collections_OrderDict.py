N=int(input())
C=[]
D=[]
E=[]
for i in range(0,N):
    C.append(input().split())
    for j in range(0,(len(C[i])-1)):
        if(j==0):
            D.append(C[i][0])
        else:
            D[i]= D[i]+' '+C[i][j]
F=[]
for i in range(0,N):
    Count=D.count(D[i])
    E.append(D[i]+' '+str(Count*int(C[i][-1])))
    if E[i] not in F:
        print(E[i])
        F.append(E[i])
#E=set(E)
