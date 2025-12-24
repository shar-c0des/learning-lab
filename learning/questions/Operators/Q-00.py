#Clearance sale 
'''
Docstring for learning.questions.Operators.Q-00
'''

price = float(input())
discount_percent = int(input())/ 100
shipping_fee = int(input())

discount_dollars = price * discount_percent
discount = price - discount_dollars

total = discount + shipping_fee 
print(round(total))
