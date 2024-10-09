def avreage_of_three_number(a,b,c):
    c=a+b+c
    d=c/3
    return d

a,b,c =map(int,input().split())
r=avreage_of_three_number(a,b,c)
print(r)