# Get starting scoreboard.
scoreboard = []
for i in range(7):
    row = input()
    scoreboard.append([i for i in row])

# Add or remove items from the scoreboard.
def process(operation):
    for i in range(7):
        row = input()
        for j, char in enumerate(row):
            if char in "~|":
                scoreboard[i][j] = [" ",char][operation == "Add:"]

# Process the additions or subtractions.
for i in range(2):
    process(input())

# Convert from scoreboard to values.
numbers = {
"  ~~~      |  ~~~      |  ~~~ ": 3,
"  ~~~      |           |      ": 7,
"  ~~~  |      ~~~      |  ~~~ ": 5,
"  ~~~  |   |       |   |  ~~~ ": 0,
"  ~~~  |   |  ~~~      |  ~~~ ": 9,
"  ~~~  |      ~~~  |   |  ~~~ ": 6,
"  ~~~  |   |  ~~~  |   |  ~~~ ": 8,
"       |   |  ~~~      |      ": 4,
"  ~~~      |  ~~~  |      ~~~ ": 2,
"           |           |      ":1}

# Get string representation of scoreboard number.
num1 = ""
num2 = ""
for i in scoreboard[1:-1]:
    num1 += "".join(i[1:7])
    num2 += "".join(i[9:15])

# Print the score.
print(f"{numbers[num1]}{numbers[num2]}")
