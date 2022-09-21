import random
list = [random.randint(0,100) for i in range(1000)]
liste2 = []
for i in list:    
    if i<10:
        liste2.append(i)
print(liste2)

