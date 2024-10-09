n = input("GIve your string : ")

def reverse_string(n):
    for i in range(len(n) - 1, -1, -1):
        print(n[i],end="")


reverse_string(n)