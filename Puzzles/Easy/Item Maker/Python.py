# Hashmap of information based on rarity.
# Corners (TL TR BL BR), top border, middle_seperator, item_name_border, skills border, bottom_seperator
border = {
"Common":[["#","#","#","#"], "#", "#", "#", "#" , "#"],
"Rare":[["/","\\","\\","/"], "#", "#", "#", "#" , "#"],
"Epic":[["/","\\","\\","/"], "-", "-", "|", "|", "_"],
"Legendary0":[["X","X","X","X"], "-", "\\__/", "[", "|", "_"],
"Legendary1":[["X","X","X","X"], "-", "\\_/", "[", "|" , "_"]}

# Hashmap for lengendary item name.
reverse = {"[":"]"}

# Get information.
name, rarity, *data = input().split(",")
data_max_length = 0
# Get max size of info.
for info in data+[name+"--"]+[rarity]:
    data_max_length = max(data_max_length , len(info)+2)

# Get correct information based on the the rarity.
info = ""
if rarity != "Legendary":
    info = border[rarity]
else:
    info = border[rarity+str(data_max_length%2)]
tl, tr, bl, br = info[0]
top_border, middle_seperator, item_name_border, skills_border, bottom_seperator = info[1:]

# Top Bar
if rarity == "Legendary":
    print(f"{tl}{top_border * ((data_max_length)//2-len(middle_seperator)+2)}{middle_seperator}{top_border * ((data_max_length)//2-len(middle_seperator)+2)}{tr}")
else:
    print(f"{tl}{top_border * (data_max_length)}{tr}")

# Item Name
padding_left , padding_right = (data_max_length-2 - len(name) + 1) // 2, (data_max_length-2 - len(name)) // 2
print(f"{item_name_border}{' '*padding_left}-{name}-{' '*padding_right}{reverse.get(item_name_border,item_name_border)}")

# Item Rarity
padding_left, padding_right = (data_max_length-2 - len(rarity) + 1) // 2 + 1, (data_max_length-2 - len(rarity)) // 2 + 1
print(f"{skills_border}{' '*padding_left}{rarity}{' '*padding_right}{skills_border}")

# Skills
for skill in data:
    print(f"{skills_border} {skill.replace(':',' ')}{' '*(data_max_length-2 - len(skill) + 1)}{skills_border}")

# Bottom Bar
print(f"{bl}{bottom_seperator*(data_max_length)}{br}")
