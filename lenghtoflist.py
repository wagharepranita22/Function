def list_length(li):
    length = len(li)
    return length

li =[]
while True:
    a = input("For adding elements in list \"Yes\" and for exit \"No\" :").lower()
    if a == "yes":
        b = input("Enter your element of list : ")
        li.append(b)
    else:
        break

print(li)


l = list_length(li)
print(f"Length of list  = {l}")
