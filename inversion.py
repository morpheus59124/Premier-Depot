numbers=[1, "test", 0.9867, "Python, c'est génial !"]
print(numbers)
def inversion(nb):
    newList = nb[::-1]
    return newList
print(inversion(numbers))