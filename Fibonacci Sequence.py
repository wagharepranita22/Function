n = int(input("n : "))
li = []
def fibonacci_Sequence(n):
    if n < 0 :
        return "incorrect input"
    elif n == 0:
        return [0]
    elif n == 1:
        return [0,1]
    else:
        li = fibonacci_Sequence(n-1)
        li.append((li[-1])+(li[-2]))
        return li



print(fibonacci_Sequence(n))

