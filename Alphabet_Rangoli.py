def print_rangoli(size):
    arr="abcdefghijklmnopqrstuvwxyz"
    for i in range(1,2*size):
      if(i<=size): 
        a=''
        for j in range(size-i+1,1,-1):
            a+='--'
        c=''
        b=size-1
        for k in range(i,1,-1):
            c+=arr[b]+'-'
            b-=1
        d=''
        b=size-1
        for k in range(i,1,-1):
            d='-'+arr[b]+d
            b-=1
        e=''
        for j in range(size-i+1,1,-1):
            e+='--'
        print(a+c+arr[size-i]+d+e)
      else:
        a=''
        for j in range(0,i-size):
            a+='--'
        b=size-1
        d=''
        for k in range(1,(2*size)-i):
          if(b>=0):  
            d=d+arr[b]+'-'
            b-=1
        b=i-size+1
        e=''
        for k in range(1,(2*size)-i):
          if(b<size):  
            e=e+'-'+arr[b]
            b+=1
        f=''
        for j in range(0,i-size):
            f+='--'
        print(a+d+arr[i-size]+e+f)
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
