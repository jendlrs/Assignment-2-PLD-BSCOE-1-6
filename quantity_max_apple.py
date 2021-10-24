money= int(input("\n Enter the amount of money you have: \n>"))
cost_per_apple= int(input("\n Price per apple: \n>"))

max_quantity= money//cost_per_apple
total= max_quantity*cost_per_apple
change= money-total

print(f"\n You can buy {max_quantity} apples and your change is {change}. \n")
