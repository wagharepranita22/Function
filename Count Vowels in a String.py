str = input("give your string  : ").lower()


def check_vowel(str):
    vow=[]
    for i in str:
        if i in "aeoie":
            if i in vow:
                continue
            else:
                vow.append(i)
    for i in vow:
        print(i ,end=" ")

check_vowel(str)
