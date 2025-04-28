def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        mod = num % i
        print(mod)
        if  mod == 0:
            return False
    return True
print(is_prime(25))