a=input()
N=int(a.split()[0])
for i in range(1,N+1):
 if(i<N/2):
    b=''
    for j in range(int((N+1)/2)-i,0,-1):
        b=b+'---'
    #print(b)
    c=''
    for k in range(1,(2*i),1):
        c=c+'.|.'
    #print(c)
    d=''
    for l in range(int((N+1)/2)-i,0,-1):
        d=d+'---'    
    print(b+c+d)
 elif(i==(N+1)/2):
    a='-' 
    print(a*int(((3*N)-7)/2)+'WELCOME'+a*int(((3*N)-7)/2))
 elif(i>N/2):
    b=''
    for j in range(1,1+i-int((N+1)/2)):
        b=b+'---'
      #  print(b)
    c=''
    for k in range(1,2*(N+1-i)):
        c=c+'.|.'
    d=''
    for j in range(1,1+i-int((N+1)/2)):
        d=d+'---'
    print(b+c+d)
