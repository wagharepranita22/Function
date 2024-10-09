# def list_length(li):
#     print(li,end=" ")
#
#
# li =[]
# while True:
#     a = input("For adding elements in list \"Yes\" and for exit \"No\" :").lower()
#     if a == "yes":
#         b = input("Enter your element of list : ")
#         li.append(b)
#     else:
#         break
#
#
#
# l = list_length(li)
def list_show(li, n):
    for i in range(n):
        print(li[i], end=" ")


li = []
n = int(input("length of list :"))
for i in range(n):
    b = input("Enter your element of list : ")
    li.append(b)

list_show(li, n)