# Get information.
leap_year = int(input())
inputs = input().split()
source_day_of_week = inputs[0]
source_month = inputs[1]
source_day_of_month = int(inputs[2])
inputs = input().split()
target_month = inputs[0]
target_day_of_month = int(inputs[1])

# Months converter, months array and days converter.
months_converter = "Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec".split(", ")
if leap_year:
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
else:
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
days = "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday".split(", ")

# Get index of months and days.
current_month_id = months_converter.index(source_month)
target_month_id = months_converter.index(target_month)
current_day_id = days.index(source_day_of_week)

# Target is after
if current_month_id < target_month_id or (current_month_id == target_month_id and target_day_of_month > source_day_of_month):
    while target_day_of_month != source_day_of_month or current_month_id != target_month_id:
        source_day_of_month += 1
        current_day_id = (current_day_id + 1)%7
        if source_day_of_month > months[current_month_id]:
            source_day_of_month = 1
            current_month_id += 1
    print(days[current_day_id])
# Target is before
else:
    while target_day_of_month != source_day_of_month or current_month_id != target_month_id:
        source_day_of_month -= 1
        current_day_id = (current_day_id - 1)%7
        if source_day_of_month < 1:
            current_month_id -= 1
            source_day_of_month = months[current_month_id]
    print(days[current_day_id])
