quantity_apples= int(input("\n How many apples do you want to buy? \n> "))
quantity_oranges= int(input("\n How many oranges do you want to buy? \n> "))

cost_per_apple= 20
cost_per_orange= 25

total= cost_per_apple*quantity_apples + cost_per_orange*quantity_oranges

print(f"\n The total amount is {total}. \n")