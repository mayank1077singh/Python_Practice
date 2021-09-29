A=input().split()
B=input().split()
#print(A)
#print(B)
C=''
for i in range(0,len(A)):
    for j in range(0,len(B)):
        if(i==0):
            C=C+'('+A[i]+', '+B[j]+') '
        else:
            C=C+'('+A[i]+', '+B[j]+') '
print(C)

