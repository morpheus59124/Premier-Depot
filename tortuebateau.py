
# Taking milles input from the user
miles = float(input("Entrer le nombre de miles: "))

# conversion factor
conv_fac = 1.62

# calculate miles
kilometres = miles * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometres,miles))