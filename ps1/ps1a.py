annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))

portion_down_payment = 0.25
current_savings = 0
r = 0.04

months = 0
down_payment = total_cost * portion_down_payment

while current_savings < down_payment:
    investment = current_savings * (r / 12)
    current_savings += ((annual_salary / 12) * portion_saved) + investment
    months += 1

print(f'Number of months: {months}')
