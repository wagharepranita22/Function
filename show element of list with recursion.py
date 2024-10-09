def show_element(li, n = 0):
    if n == len(li):
        return "end"
    print(li[n], end=" ")
    show_element(li, n+1)


li = []
n = int(input("length of list :"))
for i in range(n):
    b = input("Enter your element of list : ")
    li.append(b)
show_element(li)