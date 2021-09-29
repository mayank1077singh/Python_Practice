if __name__ == '__main__':
    N = int(input())
    Y=[]
    for i in range(0,N):
        X=input().split(" ")
        if(X[0]=="insert"):
            Y.insert(int(X[1]),int(X[2]))
        if(X[0]=="print"):
            print(Y)
        if(X[0]=="remove"):
            Y.remove(int(X[1]))
        if(X[0]=="append"):
            Y.append(int(X[1]))
        if(X[0]=="sort"):
            Y.sort()
        if(X[0]=="pop"):
            Y.pop()
        if(X[0]=="reverse"):
            Y.reverse()
