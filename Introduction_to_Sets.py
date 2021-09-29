def average(array):
    sum=0
    array1=[]
    for x in array:
        if x not in array1:
            array1.append(x)
    for i in range(0,len(array1)):
        sum+=int(array1[i])
    return(sum/(len(array1)))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
