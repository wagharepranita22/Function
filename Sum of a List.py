n =  int(input("n :"))
li= []
for i in range(n):
    a = int(input("a :"))
    li.append(a)

def sum_of_list(li):
    sum = 0
    for i in li:
        sum +=i
    return sum


print(sum_of_list(li))

