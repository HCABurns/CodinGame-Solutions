# Slightly cheating using date import.
from datetime import date

# Get first date.
day,month,year = map(int,input().split("."))
day_1 = date(year,month,day)

# Get second date.
day,month,year = map(int,input().split("."))
day_2 = date(year,month,day)

# Calculate the number of days, months and years.
days = (day_2-day_1).days
years = (day_2-day_1).days // 365
months = ((day_2.year - day_1.year) * 12 + day_2.month - day_1.month )% 12
if day_2.day < day_1.day:
    months -= 1 

# Format the years, months and days as required.
a = f"{[years,''][years==0]}{[' year',''][years == 0]}{['s',''][years<=1]}"
b = f"{[months,''][months ==0]}{[' month',''][months ==0]}{['s',''][months<=1]}"
c = f"total {days} days"
f = [a,b,c]

# Print number of years, months and days between them.
print(", ".join([i for i in f if i != ""]))
