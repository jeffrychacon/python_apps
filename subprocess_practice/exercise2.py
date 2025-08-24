str1 = '''{[([])]]}'''
ls1 = list(str1)
print(ls1)
ls2=[]
for i, el in enumerate(ls1): 
    print(el)
    if el == '}' or el == ']' or el ==')':
        ls2.append(el)
        ls1.pop(i)
print(ls1)
print(ls2)

for el in ls1:
    for i, el2 in enumerate(ls2):
        print(f"el1 {el} and el2 {el2}")
        print(i)
        if el == '{' and el2 =='}':
            ls2.pop(i)
        if el == '[' and el2 ==']':
            ls2.pop(i)
        if el == '(' and el2 ==')':
            ls2.pop(i)
print(ls2)