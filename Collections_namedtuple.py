N=int(input())
Arr=[]
Sum=0
Arr.append(input().split())
for j in range(0,4):
        if(Arr[0][j]=='MARKS'):
            break
for i in range(1,N+1):
    Arr.append(input().split())
    Sum=Sum+int(Arr[i][j])
print(round((Sum/N),2))
