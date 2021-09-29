if __name__ == '__main__':
    list1 = []
    min1=99.0
    j=0
    min2=100.0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list = [name,score]
        if score < min1:
  
           min2=min1
           min1=score
        if score <min2 and score>min1:
            min2=score
        
        list1 = list1+[list]
        j=j+1
    if min2==99.0:
        min2=min1

    for i in list1[ : :-1]:
        if list1[j-1][1]==min2:
           print(list1[j-1][0])
        j=j-1
        if j<0:
            break

