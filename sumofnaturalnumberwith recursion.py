def sumofnumber(n):
    if n == 0:
        return 0
    else:
        return n + sumofnumber(n-1)


n = int(input("gie your number range to calculate : "))
print(sumofnumber(n))