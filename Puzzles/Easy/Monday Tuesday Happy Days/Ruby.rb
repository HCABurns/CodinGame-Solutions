# Get information.
leap_year = gets.to_i
source_day_of_week, source_month, source_day_of_month = gets.split
source_day_of_month = source_day_of_month.to_i
target_month, target_day_of_month = gets.split
target_day_of_month = target_day_of_month.to_i

# Months converter, months array and days converter.
months_converter = "Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec".split(", ")
if leap_year == 1
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
else
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
end
days = "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday".split(", ")

# Get index of months and days.
current_month_id = months_converter.index(source_month)
target_month_id = months_converter.index(target_month)
current_day_id = days.index(source_day_of_week)

# Target is after
if current_month_id < target_month_id || (current_month_id == target_month_id && target_day_of_month > source_day_of_month)
    while target_day_of_month != source_day_of_month || current_month_id != target_month_id do
        source_day_of_month += 1
        current_day_id = (current_day_id + 1)%7
        if source_day_of_month > months[current_month_id]
            source_day_of_month = 1
            current_month_id += 1
        end
    end
# Target is before
else
    while target_day_of_month != source_day_of_month || current_month_id != target_month_id do
        source_day_of_month -= 1
        current_day_id = (current_day_id - 1)%7
        if source_day_of_month < 1
            current_month_id -= 1
            source_day_of_month = months[current_month_id]
        end
    end
end

# Print day of the week for target day.
puts days[current_day_id]
