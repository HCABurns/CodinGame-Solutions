# Generate email.
email = ""
for _ in range(int(input())):
    email += input()+"\n"

# Variables to be used.
choice_indicator = 0
out = ""
pos = 0

# Generate email selecting a choice if available.
while pos < len(email):
    # Add chars until a choice occurs.
    while pos < len(email) and email[pos]!="(":
        out += email[pos]
        pos += 1
    # Find end of the choices.
    end = pos
    if pos < len(email):
        while end < len(email) and email[end] != ")":
            end += 1
        # Add correct choice and updated variables.
        out += email[pos+1:end].split("|")[choice_indicator%len(email[pos+1:end].split("|"))]
        choice_indicator += 1
        pos = end + 1

# Print the new email.
print(out)
