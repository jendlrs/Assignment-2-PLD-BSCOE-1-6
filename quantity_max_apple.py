money= float(input("\n Enter the amount of money you have: \n> "))
cost_per_apple= float(input("\n Price per apple: \n> "))

max_quantity= int(money/cost_per_apple)
change= money % cost_per_apple

print(f"\n You can buy {max_quantity} apples and your change is {change:.2f} pesos. \n")
