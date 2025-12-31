print("Welcome to Simple Rent Calculator")
monthly_rent = int(input("Enter the monthly  Flat rent amount: "))

food = int(input("Enter the amount of food ordered= "))

how_much_units_spend = int(input("Enter the total electricity units spent= "))

charge_per_unit = int(input("Enter the charge per unit= "))

persons = int(input("Enter the number of Persons for living the flat/ room= "))


Total_rent = monthly_rent + food + how_much_units_spend + (charge_per_unit * 30)


Output = (food + monthly_rent + how_much_units_spend + (charge_per_unit * 30)) / persons

print("Total rent for the month is: ", Total_rent)
print("Each person has to pay: ", Output)
print("Thank you !!")

