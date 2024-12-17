import random

# List of gifts grouped by material
gifts = {
    "metal": [
        "toy train", 
        "silver bracelet", 
        "soldier figurine", 
        "steel lunchbox", 
        "brass trumpet", 
        "yo-yo", 
        "stainless steel water bottle", 
        "pocket knife", 
        "metallic keychain", 
        "model airplane"
    ],
    "wooden": [
        "rocking horse", 
        "carved chess set", 
        "building blocks", 
        "handmade puzzle", 
        "toy car", 
        "abacus", 
        "dollhouse", 
        "spinning top", 
        "train set", 
        "handcrafted birdhouse"
    ],
    "plastic": [
        "doll", 
        "action figure", 
        "toy robot", 
        "building bricks", 
        "colorful frisbee", 
        "beach bucket and spade", 
        "dinosaur figure", 
        "race car", 
        "water gun", 
        "tea set"
    ],
    "paper": [
        "origami set", 
        "storybook", 
        "airplane kit", 
        "coloring book", 
        "gift wrapping paper", 
        "notepad", 
        "stationery set", 
        "lanterns", 
        "pop-up greeting card", 
        "scrapbook"
    ],
    "electronic": [
        "remote control car", 
        "tablet", 
        "gaming console", 
        "digital watch", 
        "wireless headphones", 
        "smart speaker", 
        "toy piano", 
        "VR headset", 
        "digital camera", 
        "handheld gaming device"
    ],
    "glass": [
        "ornament", 
        "crystal snow globe", 
        "vase", 
        "stained glass lamp", 
        "marbles", 
        "picture frame", 
        "perfume bottle", 
        "candle holder", 
        "drinking cup", 
        "decorative bowl"
    ]
}


types = "paper, electronic, glass, metal, wooden, plastic, ".split(", ")

new_items = []

n = 9+6
print(n)

# Add one of each item.
for material, items in gifts.items():
    pos = random.randint(0,len(items)-1)
    new_items.append(f"{items[pos]},{material}") 

# Add items until at n.
while len(new_items) != n:
    type = types[random.randint(0,len(types)-1)]
    pos = random.randint(0,len(gifts[type])-1)
    if f"{gifts[type][pos]},{type}" not in new_items:
        new_items.append(f"{gifts[type][pos]},{type}")

for item in new_items:
    print(item)
