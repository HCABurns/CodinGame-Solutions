# Store players and their stats.
players = {"KEN":[25,6,5], "RYU":[25,4,5],"TANK":[50,2,2],"VLAD":[30,3,3],"JADE":[20,2,7],"ANNA":[18,9,1],"JUN":[60,2,1]}

# Class to hold player information.
class Player:
    def __init__(self,name, hp ,punch, kick):
        self.name = name
        self.hp = hp
        self.attack = {"PUNCH":punch,"KICK":kick}
        self.rage = 0
        self.hits = 0
        self.damage_taken = 0

    def hurt(self,amount):
        self.rage += 1
        self.damage_taken += amount
        self.hp -= amount

    def special(self, opp):
        spec = {"KEN":3*self.rage, "RYU":4*self.rage, "TANK":2*self.rage,
        "VLAD":2*(self.rage+opp.rage),
        "JADE":self.hits*self.rage,
        "ANNA": self.damage_taken*self.rage,
        "JUN": self.rage}[self.name]

        if self.name == "JUN": self.hp += self.rage
        self.rage = 0
        if self.name == "VLAD": opp.rage = 0

        return spec

# Get players.
champion_1, champion_2 = input().split()
p1 = Player(champion_1,*players[champion_1])
p2 = Player(champion_2,*players[champion_2])

# Simulate hits.
n = int(input())
for i in range(n):
    d, attack = input().split()

    if d == "<":
        p1.hurt(p2.attack[attack] if attack != "SPECIAL" else p2.special(p1))
        p2.hits+=1
    else:
        p2.hurt(p1.attack[attack] if attack != "SPECIAL" else p1.special(p2))
        p1.hits+=1

    if p1.hp <= 0 or p2.hp <= 0:
        break

# Print the winner and number of hits.
if p2.hp > p1.hp:
    p1, p2 = p2, p1
print(f"{p1.name} beats {p2.name} in {p1.hits} hits")

