from math import fabs

a = 0
while True:
    a =int(input("Press 1 if you want to calculate number of months "
                 "needed to make savings or press 2 if you want to calculate monthly savings."))
    if a == 1 or a == 2:
        break


semi_annual_raise = 0.1
current_savings = 0
r = 0.04

if a == 1:
    annual_salary = float(input("Your annual salary: "))
    portion_savings = float(input("Portion you're saving: "))
    total_cost = float(input("Total cost: "))
    number_of_months = 0

    while current_savings < total_cost:
        if number_of_months % 6 == 5:
            monthly_salary = monthly_salary + monthly_salary*0.1
        current_savings = current_savings + current_savings*r/12 + monthly_salary*portion_savings
        number_of_months+=1

    print("You need to save money for", number_of_months, "months.")
else:
    annual_salary = float(input("Your annual salary: "))
    number_of_months = float(input("Number of months you want you're planning to make savings: "))
    total_cost = float(input("Total cost: "))
    portion_savings = 0.0
    monthly_salary = annual_salary/12

    while fabs(total_cost - number_of_months*monthly_salary*portion_savings) > 100:
        if total_cost > number_of_months*monthly_salary*portion_savings:
            portion_savings+=0.001
        else:
            portion_savings-=0.001
    print("You need to save", monthly_salary*portion_savings, "a month!")
