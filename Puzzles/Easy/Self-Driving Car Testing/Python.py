# Get number of commands.
n = int(input())

# Create array of commands.
xthen_commands = input()
num_of_commands, *commands = xthen_commands.split(";")
c = []
pos = int(num_of_commands)-1
for command in commands:
    num = int("".join([i for i in command if i.isnumeric()]))
    c+=[command[-1]]*num
c = c[::-1]

# place the car position on the road based on commands.
for i in range(n):
    rthen_roadpattern = input()
    N , pattern = rthen_roadpattern.split(";")
    for _ in range(int(N)):
        command = c.pop()

        if command == "R":
            pos += 1
        if command == "L":
            pos -= 1
        
        # Add car and print.
        p = list(pattern)
        p[pos] = "#"
        print("".join(p))
