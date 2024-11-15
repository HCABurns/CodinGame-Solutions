def number_to_column(value)
  """
  Helper function to convert from decimal to spreadsheet column.

  Parameter:
  value : int - Value to be converted.

  Return: String - String of corresponding spreadsheet column.
  """
  # Ensure not 0 input.
  if value==0
    print("A")
    exit!
  end

  # Set output.
  column_name = ""

  # Continue until converted from base 10 to base len(c)
  while value > 0
      value -= 1
      # Regular base conversion
      rem = value % 26
      column_name += ("A".ord + rem).chr
      value = (value / 26).floor
  end
  return column_name
end


def column_to_number(column)
  """
  Helper function to convert from spreadsheet column to decimal.

  Parameter:
  column : String - Column to be converted.

  Return: int - Int of corresponding spreadsheet column.
  """
  # Set total variable.
  total = 0
  # Convert from base 26 to decimal.
  column.each_char.with_index{|j , i| total += (j.ord-"A".ord+1) * (26 ** i)}
  return total
end


# Define array to store conversions.
conversions = []
n = gets.to_i
gets.chomp.split.each do |label|
  # Select correct function to swap column and decmial.
  conversion = nil
  if label.to_i.to_s == label
    conversion = number_to_column(label.to_i).reverse
  else
    conversion = column_to_number(label.reverse)
  end
  # Add to array
  conversions << conversion
end

# Output the conversions.
puts conversions.join(" ")
