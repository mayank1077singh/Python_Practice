from array import *
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list1 = list(arr)
    new_list = set(list1) 
    new_list.remove(max(new_list)) 
    print(max(new_list)) 
