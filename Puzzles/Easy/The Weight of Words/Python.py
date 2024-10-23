#Get required inputs
steps = int(input())
h = int(input())
w = int(input())
rows = []
w = []
rows = [list(input()) for _ in range(h)]

for _ in range(steps):
    #Calculate the column weights
    w2 = [0 for _ in range(len(rows[0]))]
    for col in range(len(rows[0])):
        for row in range(len(rows)):
            w2[col] += ord(rows[row][col])
    
    #Move each column by X amount
    for column,weight in enumerate(w2):
        shift_amount = weight % len(rows)
        for _ in range(shift_amount):
            new = []
            for i in range(len(rows)):
                new+=[rows[i][column]]
            new = [new[-1]]+new[:-1]
            for i,v in enumerate(new):
                rows[i][column] = v

    #Calculate new row weights
    w = []
    for row in rows:
        w.append(sum(ord(c) for c in row))

    #Move the rows by X amount
    for i,weight in enumerate(w):
        for _ in range(weight%len(rows[0])):
            rows[i] = [rows[i][-1]] + rows[i][:-1]

#Output the rows
for i in range(h):
    print(*rows[i],sep="")
