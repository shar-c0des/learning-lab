
#given input for meal cost, tip & tax percent 
meal_cost = float(input().strip())
tip_percent = int(input().strip())
tax_percent = int(input().strip())

# calculate the tip and tax percent
tip = tip_percent * meal_cost / 100
taxes = tax_percent * meal_cost / 100

# total cost of meal rounded to the nearest integer
total_cost = meal_cost + tip + taxes
print(f'Total cost: {round(total_cost)}')
