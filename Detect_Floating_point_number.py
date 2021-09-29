N=int(input())
for i in range(0,N):
    g=input()
    try:
        float(g)
    except ValueError:
        print('False')
    else:
        if(len(g.split("."))>1):
            print('True')
        else:
            print('False')
