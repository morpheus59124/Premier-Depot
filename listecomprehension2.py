import random
list = [random.randint(0,100) for i in range(1000)]
liste2 = [i for i in list if i<10]
print(liste2)

