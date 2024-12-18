# Generate email.
email = ""
gets.to_i.times do
  email += gets.chomp + "\n"
end
email = email[0,email.size-1]
# Variables to be used.
choice_indicator = 0
out = ""
pos = 0

while pos < email.size do
  # Add chars until a choice occurs.
  while pos < email.size && email[pos]!="("
    out += email[pos]
    pos += 1
  end
  # Find end of the choices.
  end_pos = 0
  if pos < email.size
    while pos+end_pos < email.size && email[pos+end_pos] != ")" do
      end_pos += 1
    end
    # Add correct choice and updated variables.
    choices = email[pos+1,end_pos-1]
    choices += " " if choices.end_with?("|")
    out += choices.split("|")[choice_indicator%choices.split("|").size].rstrip
    choice_indicator += 1
    pos += end_pos + 1
  end
end

# Print the new email.
puts out
