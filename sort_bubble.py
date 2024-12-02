import random

def sorting(ls1):
    i = 0
    while(i<len(ls1)-1):
        if(ls1[i] > ls1[i+1]):
            ls1[i],ls1[i+1] = ls1[i+1],ls1[i]
            sorting(ls1)
        i += 1
    return ls1

random_numbers = [random.randint(1,100) for _ in range (20)]
print(random_numbers)
print(sorting(random_numbers))