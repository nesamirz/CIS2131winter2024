Name = input("enter the name:")
print("Name:",Name)
Hourly_wages = int(input("enter hourly_wages"))
Hours_worked = int(input("enter hours_worked"))
print("Name:",Name)
weekly_salary_before_taxes =(Hourly_wages * Hours_worked)
print("weekly_salary_before_taxes:",weekly_salary_before_taxes)
taxes = weekly_salary_before_taxes * 10/100
print("taxes:", taxes)
net_salary = int(weekly_salary_before_taxes - taxes)
print("net_salary:", net_salary)