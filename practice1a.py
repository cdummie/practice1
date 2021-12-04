annual_salary = float(input("Your annual salary: "))
portion_savings = float(input("Portion you're saving: "))
total_cost = float(input("Total cost: "))

monthly_salary = annual_salary/12
current_savings = 0
r = 0.04
number_of_months = 0

while current_savings < total_cost:
    current_savings = current_savings + current_savings*r/12 + monthly_salary*portion_savings
    number_of_months+=1

print("You need to save money for", number_of_months, "months.")
