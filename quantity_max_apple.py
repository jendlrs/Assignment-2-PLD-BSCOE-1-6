money= int(input("\n Enter the amount of money you have: \n>"))
cost_per_apple= int(input("Price per apple: "))

max_quantity= money/cost_per_apple
total=max_quantity*cost_per_apple

print(f"You can buy {max_quantity} apples and your change is ")
