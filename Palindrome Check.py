str = input("give your string  : ").lower()


def is_pallindrome(str):
    copy= str
    a=""
    for i in range(len(str)-1,-1,-1):
        a+=str[i]

    if a == copy:
        print("String is pallindrome")
    else:
        print("String is not pallindrome")



is_pallindrome(str)