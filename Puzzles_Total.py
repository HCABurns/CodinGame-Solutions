"""
This script will use the https://chadok.info/codingame/ website to retrieve information about a players puzzles.
The result will be the total number of puzzles solved in all languages, split by difficulty.

How to find your player_id:
1. Open the provided link in a web browser: https://chadok.info/codingame/
2. Find option 7 at the bottom of the main menu and enter your codingame username. If your name appears in a button go to step 3b, otherwise 3a.
3a. Go to your codingame profile and get the url.
3ai. Take the last section of the url and paste in in the new input box at the bottom of the page then move to section 3b.
     e.g. for https://www.codingame.com/profile/mk4ig8...3863 - The useful information is mk4ig8...3863
3b. Simply click on the button containing your username.
3bi. There will be three option boxes, the last option box containing only numbers.
"""

# Required imports
from requests import get
from re import findall, search

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# -=-=-=-=-=-=-=-=- YOUR PLAYER ID GOES HERE! -=-=-=-=-=-=-=-=- #
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# Player ID
#player_id = 5192217
player_id = None
assert player_id != None, "No player ID provided!\nPlease follow the instructions at the top of the file or use player_id = 5192217 as an example."

# Get and display name player name associated with the player_id
url = f"https://chadok.info/codingame/players_puzzles.php?level=easy&commu=0&player={player_id}&update=0"
data = get(url)
if data.status_code == 200:
    pattern = r'player <a href="[^"]*">([^<]+)</a>'
    name = search(pattern, data.text)
    if name:
        print(f"Showing results for: {name.group(1)}\n")
    else:
        print("No player name found...")

# URLS
tutorial = [f"https://chadok.info/codingame/players_puzzles.php?level=tutorial&commu=0&player={player_id}&update=0","Tutorial"]
easy_cg = [f"https://chadok.info/codingame/players_puzzles.php?level=easy&commu=0&player={player_id}&update=0", "Easy CG Solutions"]
easy_community = [f"https://chadok.info/codingame/players_puzzles.php?level=easy&commu=1&player={player_id}&update=0","Easy Community Solutions"]
medium_cg = [f"https://chadok.info/codingame/players_puzzles.php?level=medium&commu=0&player={player_id}&update=0","Medium CG Solutions"]
medium_community = [f"https://chadok.info/codingame/players_puzzles.php?level=medium&commu=1&player={player_id}&update=0","Medium Community Solutions"]
hard_cg = [f"https://chadok.info/codingame/players_puzzles.php?level=hard&commu=0&player={player_id}&update=0","Hard CG Solutions"]
hard_community = [f"https://chadok.info/codingame/players_puzzles.php?level=hard&commu=1&player={player_id}&update=0","Hard Community Solutions"]
expert_cg = [f"https://chadok.info/codingame/players_puzzles.php?level=expert&commu=0&player={player_id}&update=0","Expert CG Solutions"]
expert_community = [f"https://chadok.info/codingame/players_puzzles.php?level=expert&commu=1&player={player_id}&update=0","Expert Community Solutions"]

# Iterate through each difficulty level for community and official CodinGame puzzles and find total number of puzzles solved.
urls = [tutorial, easy_cg, easy_community, medium_cg, medium_community, hard_cg, hard_community, expert_cg, expert_community]
totals = []
solved = []
total = 0
for url_info in urls:
    # Get data.
    url, identifier = url_info
    data = get(url)
    # Ensure response from website.
    if data.status_code == 200:
        # Find total of completed puzzles for `identifier`.
        local_total = 0
        local_solved = 0
        for val in findall("<th>[0-9]+</th>",data.text):
            val = val.replace("<th>","").replace("</th>","")
            if val.isnumeric():
                local_total += int(val)

        # Find total of individual completed puzzles for `identifier`.
        for val in findall("<td>[0-9]+</td>",data.text):
            val = val.replace("<td>","").replace("</td>","")
            if val.isnumeric():
                if int(val) != 0:
                    local_solved += 1
            
        # Output and store total.
        print(f"Total for {identifier}: {local_total}")
        total+=local_total
        totals+=[local_total]
        solved += [local_solved]
    else:
        print(f"Error! Could not retrieve data for {identifier}... Error Code: {data.status_code}")

# Print number of individual puzzles solved for each category. (Classify tutorial as easy)
print()
solved[1] += solved[0]
for i,name in zip(range(1,len(solved),2),["Easy","Medium","Hard","Expert"]):
    print(f"Total individual {name} puzzles solved: {solved[i]+solved[i+1]}")


# Print combined totals for community and official CodinGame puzzles.
print()
totals[1] += totals[0] #NOTE: Keep to also include tutorial as an Easy puzzle (Technically classified as one).
print("Total for tutorial:",totals[0])
for i,name in zip(range(1,len(totals),2),["Easy","Medium","Hard","Expert"]):
    print(f"Total {name} solutions: {totals[i]+totals[i+1]}")
print()

# Print total of all difficulty levels for community and official CodinGame puzzles.
print(f"Total solved in all languages: {total}")
