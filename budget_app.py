

print"Please enter your monthly income: "
month_income = raw_input()

print"Enter your phone bill: "
phone_bill= raw_input()

print"Enter weekly food expense: "
food_expense= raw_input()


def budget_calc(month_income, phone_bill, food_expense):
    savings_calc= float(month_income) - (float(phone_bill) + float(food_expense))
    return savings_calc

print "The amount of money that should go into your savings is: ", budget_calc(month_income, phone_bill, food_expense)
 