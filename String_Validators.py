if __name__ == '__main__':
    s = input()
    a=False
    b=False
    c=False
    d=False
    e=False
    for i in s:
        for j in range(0,len(s)):
            a=a or s[j].isalnum()
            b=b or s[j].isalpha()
            c=c or s[j].isdigit()
            d=d or s[j].islower()
            e=e or s[j].isupper()
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

