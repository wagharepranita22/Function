a, b, c =map(int,input().split())

def largest_number(a , b, c):
    if a < c and b < c:
        print(f"{c} is greater number")
    elif b < a and c < a:
        print(f"{a} is greater number")
    else:
        print(f"{b} is greater number")


largest_number(a,b,c)