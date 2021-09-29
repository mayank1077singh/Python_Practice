X=input().split(" ")
A=[]
B=[]
for i in range(0,int(X[0])):
    A.append(input().split(" "))
#print(A)
for j in range(0,int(X[1])):
    B.append(input().split(" "))
#print(X[1])
for i in range(0,int(X[1])):
    C=''
    for j in range(0,int(X[0])):
        if(A[j]==B[i]):
            C=C+str(j+1)+' '
    if(len(C)):
        print(C)
    else:
        print("-1")
    
