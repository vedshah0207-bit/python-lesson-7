units_used = int(input("Enter the number of units of electricity consumed."))

if units_used <= 50:
    cost = units_used * 2.60
    tax = 25
elif units_used <= 100:
    cost = 130 + ((units_used - 50) * 3.25)
    tax = 35
elif units_used <= 200:
    cost = 130 + 162.5 + ((units_used - 50) * 5.26)
    tax = 45
else:
    cost = 130 + 162.5 + 526 + ((units_used - 50) * 8.45)
    tax = 75

total = cost + tax

print("Your electricity bill %.2f" %total) #%.2f means it will round to 2 decimal places.