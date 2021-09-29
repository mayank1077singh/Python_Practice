import re
N=int(input())
for i in range(0,N):
    X=input()
    try:
        re.compile(X)
    except:
        print("False")
    else:
        print("True")
