import string

mydic = {}
alpha = list(string.ascii_lowercase)

for el in range(20):
    if not mydic:
        mydic[0]= alpha[0]
    else:
        mydic[el] = alpha[el]

print(mydic)