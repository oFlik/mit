annual_salary = float(input('Enter your starting annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))

total_cost = 1000000
portion_down_payment = 0.25
current_savings = 0
semi_annual_raise = .07
r = 0.04

months = 0
down_payment = total_cost * portion_down_payment

while current_savings < down_payment:
    months += 1

    investment = current_savings * (r / 12)
    current_savings += ((annual_salary / 12) * portion_saved) + investment

    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise

print(f'Number of months: {months}')
