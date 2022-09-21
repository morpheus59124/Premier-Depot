list =[ nb for nb in range(100)]
for nb in range(len(list)):
    if nb % 3 == 0 and nb % 5 == 0:
        print("fizz_fuzz")
    elif nb % 3 == 0:
        print("fizz")
    elif nb % 5 == 0:
        print("fuzz")
    else :
        print(nb)

    
    



