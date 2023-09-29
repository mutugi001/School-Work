#Collins Mutugi Wachira
#SCT211-0051/2022

import math

Total_bill = input("enter total bill: ")
Total_bill = int(Total_bill)
tip_amount = input("Tip percentage(10,12 or 15): ")
tip_amount = int(tip_amount)
tip_amount = tip_amount/100
number_of_people = input("number of people splitting the bill: ")
number_of_people = int(number_of_people)

total_pay = Total_bill + tip_amount
payable_amount = total_pay/number_of_people

print(round(payable_amount, 2))

