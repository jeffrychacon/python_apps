def add(*args):
    print(args[1])
    total = 0
    for n in args:
        total += n
    return total

# def calculate(**kwargs):
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#     return kwargs["add"] + kwargs["multiply"]

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2,add=3, multiply=5)
print(add(1,2,3,4,5,6,7,8,9,10))

class Car:

    def __init__(self, **kw):
        #self.make = kw["make"]
        self.make = kw.get("make")  #This way it won't give an error if the key doesn't exist
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")
    
my_car = Car(make="Nissan", model="GT-R", color="White", seats=4)
print(my_car.model)
