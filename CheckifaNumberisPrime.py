n = int(input(" n : "))


def prime_number(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        print("Number is prime ")
    else:
        print("Number is not prime")


prime_number(n=n)
