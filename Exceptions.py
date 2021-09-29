N=int(input())
X=[]
for i in range(0,N):
    X=input().split(" ")
    try:
        print(int(int(X[0])/int(X[1])))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code: {0}".format(e))
        #print(e)

