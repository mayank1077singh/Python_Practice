A=input().split(" ")
N=int(A[0])
X=int(A[1])
B=[]
for i in range(0,X):
    g=input().split(" ")
    for j in range(0,N):
        g[j]=float(g[j])
    B.append(g)
for i in range(0,N):
    sum=0
    for j in range(0,X):
        sum+=B[j][i]
    print(round(sum/X,1))

