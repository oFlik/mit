starting_salary = float(input('Enter the starting salary: '))

portion_down_payment = 0.25
total_cost = 1000000
down_payment = total_cost * portion_down_payment

semi_annual_raise = .07
r = 0.04

low = 0
high = 10000
epsilon = 100
portion_saved = (low + high) / 2

months = 36

while current_savings < down_payment:
    months += 1

    investment = current_savings * (r / 12)
    current_savings += ((annual_salary / 12) * portion_saved) + investment

    if months % 6 == 0:
        starting_salary += starting_salary * semi_annual_raise

print(f'Number of months: {months}')