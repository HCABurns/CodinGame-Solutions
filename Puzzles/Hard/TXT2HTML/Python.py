from collections import defaultdict

# Get number of rows.
n = int(input())

# Create table of content for the data.
content = defaultdict(list)
row = -1
columns = 0
for i in range(n):
    s = input()
    if s[0] == "+":
        row += 1
        columns = s.count("+")-1
    else:
        if row not in content:
            content[row] = [[] for _ in range(columns)]
        for i,text in enumerate(s.split("|")[1:-1]):
            content[row][i].append(text.strip())

# Format and print in HTML.
print("<table>")
for row in content.values():
    print(f"<tr>{''.join(['<td>'+' '.join(data).strip() +'</td>' for data in row])}</tr>")
print("</table>")
