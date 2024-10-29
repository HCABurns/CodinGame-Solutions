class Tribute:
    """
    Helper class to hold information regarding a tribute.
    """
    def __init__(self,name):
        """
        Initialise a tribute.

        Parameter:
        name:string - Name of the tribute.
        """
        self.name = name
        self.killer = ""
        self.killed = []
    def get_name(self):
        """
        Return the name of the tribute.
        """
        return self.name
    def get_killer(self):
        """
        Return tributes killer or Winner if they won.
        """
        return self.killer if self.killer != "" else "Winner"
    def get_killed(self):
        """
        Return string of players killed.
        """
        return ", ".join(sorted(self.killed)) if self.killed != [] else "None"

# Create a hashmap of the tributes.
tributes = {}
for i in range(int(input())):
    player_name = input()
    tributes[player_name] = Tribute(player_name)

# Assign the deaths and kills from the game.
for i in range(int(input())):
    # Extract relevant information from the input.
    row = input()
    row = row.replace(",","")
    killer_name, _, *killed  = row.split(" ")

    # Set kill for killer
    for kill in killed:
        tributes[killer_name].killed.append(kill)
    
    # Set killer for killed.
    for dead in killed:
        tributes[dead].killer = killer_name

# Output the results of the hunger games.
names = sorted(tributes.keys())
for name in names:
    print("Name:",tributes[name].get_name())
    print("Killed:",tributes[name].get_killed())
    print("Killer:",tributes[name].get_killer())
    if name != names[-1]:
        print()
