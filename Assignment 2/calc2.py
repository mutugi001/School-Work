#Collins Mutugi Wachira
#SCT211-0051/2022
from datetime import date

Name= input("enter name : ")

YOB=input("enter year of birth: ")
MOB=input("enter month of birth: ")
DOB=input("enter date of birth: ")
YOB=int(YOB)
MOB=int(MOB)
DOB=int(DOB)

today = date.today()
current_year = int(today.year)
current_month = int(today.month)
current_date = int(today.day)

# current_year = int(current_year)
# current_month = int(current_month)
# current_date = int(current_date)

age_in_years = str(current_year - YOB)
if current_month >= MOB:
    age_in_months = str(current_month - MOB)
else:
    age_in_months = str(12 - (MOB - current_month))
if current_date >= DOB:
    age_in_days = str(current_date - DOB)
else:
    age_in_days = str(30 - (DOB - current_date))

print(Name + " is " + age_in_years + " yrs, " + age_in_months + " months and " + age_in_days + " days old.")
