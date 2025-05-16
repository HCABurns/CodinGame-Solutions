# Hashmap for ordering the output.
order = {"Pinned":0, "Followed":1,"none":2}

# Array for the comments and a hashmap to store replies to comments.
replies = {}
comments = []

# Read in the comments and store in comments and store replies in the hashmap.
n = int(input())
prev = "---"
for i in range(n):
    comment = input()
    if comment[0] != " ":
        comments += [comment.split("|")]
        prev = comment  
    else:
        if prev in replies:
            replies[prev].append(comment.split("|"))
        else:
            replies[prev] = [comment.split("|")]

# Use a custom sort and then print the comments and replies in the correct order.
comments.sort(key = lambda a: (order[a[-1]], -int(a[2]), -int(a[1].split(":")[0]),-int(a[1].split(":")[1])))
for comment in comments:
    comment = "|".join(comment)
    print(comment)
    if comment in replies:
        reps = replies[comment]
        reps.sort(key = lambda a: (order[a[-1]], -int(a[2]), -int(a[1].split(":")[0]),-int(a[1].split(":")[1])))
        for rep in reps:
            print("|".join(rep))
