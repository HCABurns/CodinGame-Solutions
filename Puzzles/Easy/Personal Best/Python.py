# Form hashamps and arrays to be used.
athletes = {}
gymnasts = input().split(",")
categories = [["bars","beam","floor"].index(cat) for cat in input().split(",")]
n = int(input())

# Get max scores of gymnasts and store in hashmap.
for i in range(n):
    name,bars,beam,floor = input().split(",")
    if name not in athletes:
        athletes[name] = [bars,beam,floor]
    else:
        bars_pr = athletes[name][0]
        beam_pr = athletes[name][1]
        floor_pr = athletes[name][2]
        athletes[name] = [max(bars,bars_pr),max(beam,beam_pr),max(floor,floor_pr)]

# Output scores of gymnasts in given categories.
for name in gymnasts:
    output = []
    for category in categories:
        output.append(athletes[name][category])
    print(",".join(output))
