"""
This is a script for retrieval of information for a players' published puzzles on codingame.com.
Additionally, it will format it in a way to be copy and paste directly into a github readme file.

How to find your player_id:
1. Open the provided link in a web browser: https://chadok.info/codingame/
2. Find option 7 at the bottom of the main menu and enter your codingame username. If your name appears in a button go to step 3b, otherwise 3a.
3a. Go to your codingame profile and get the url.
3ai. Take the last section of the url and paste in in the new input box at the bottom of the page then move to section 3b.
     e.g. for https://www.codingame.com/profile/mk4ig8...3863 - The useful information is mk4ig8...3863
3b. Simply click on the button containing your username.
3bi. There will be three option boxes, the last option box containing only numbers.

Adding your solution with a  solutions file:
Create a python file with the name solutions and create a hashmap with the name db (db = {}).
Now populate the keys with the names of your puzzles and the value is the link to your solution file
e.g. db = {"Onboarding":"https://github.com/...", "...":"..."}
Additionally, if you wish to include source code for a solo game: {"Onboarding":[".../source_code_link","https://github.com/..."], "...":"..."}
"""

# Required imports
from requests import get
from re import search
from bs4 import BeautifulSoup
from solutions import db

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# -=-=-=-=-=-=-=-=- YOUR PLAYER ID GOES HERE! -=-=-=-=-=-=-=-=- #
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# Player ID
player_id = 5192217
assert player_id != None, "No player ID provided!\nPlease follow the instructions at the top of the file or use player_id = 5192217 as an example."


# Get and display name player name associated with the player_id
url = f"https://chadok.info/codingame/players_puzzles.php?level=easy&commu=0&player={player_id}&update=0"
data = get(url)
assert data.status_code == 200, "Failure to retrieve data from the website. Try again later or check the website status."
player_name = None
if data.status_code == 200:
    pattern = r'player <a href="[^"]*">([^<]+)</a>'
    player_name = search(pattern, data.text)
    if player_name:
        player_name = player_name.group(1)
        print(f"Showing results for: {player_name}\n")
assert player_name, "No player name found..."

# Get the information for Easy, Medium, Hard and Expert Puzzles.
url = "https://chadok.info/codingame/puzzles_list.html"
pattern = '<div class="magicDiv"[^"]*<\div>'
data = get(url)
assert data.status_code == 200, "Failure to retrieve data from the website. Try again later or check the website status."
data = data.text

# Parse the HTML
soup = BeautifulSoup(data, 'html.parser')

# Find ALL divs with class="magicDiv"
magic_divs = soup.find_all('div', class_='magicDiv')[0:4]

# Get the names

td_texts = [th.get_text(strip=True) for th in magic_divs[0].find_all("th")]

# Process each one - Storing if matching the player name
players_puzzles = []
updated = False
diff = 0
difficulty = {0:"Tutorial",1:"Easy",2:"Medium",3:"Hard",4:"Expert"}
for div in magic_divs:
    for tr in div.find_all("tr")[1:]:
        td_texts = []
        tds = tr.find_all("td")

        # Extract the tags from the hmtl
        last_td = tds[-1]
        tags = "<br>".join([a.get_text(strip=True) for a in last_td.find_all("a")])
        #print(tags)
        for td in tds:
            for span in td.find_all("span"):
                span.decompose()
            td_texts.append(td.get_text(strip=True))
        
        if td_texts[1] == player_name:
            players_puzzles.append(td_texts+[difficulty[diff]] + [tags])
            #4,6
            if players_puzzles[-1][4] or players_puzzles[-1][4]:
                if not updated:
                    print("The following puzzles have had players attempt or solve them:")
                    updated = True
                print(td_texts+[difficulty[diff]] + [tags])
    diff+=1

# Ensure there is a result
assert players_puzzles, f"No published puzzles for {player_name} found."

# Sort the display by: 0-Name, 3-Solves, 5-Attmepts, 7-Success Rate, 8-Rating, 9-Date, 11-Difficulty.
players_puzzles.sort(key = lambda x:(-float(x[5]), -float(x[8])))
# Display the information in a github table.
print("\n| <b>Name</b> | <b>Difficulty</b> | <b>Total Attempts</b> |<b>Success Rate</b> | <b>Rating</b> | <b>Tags</b> | <b>Solution</b> |<b>Status</b> |")
print("| :---------: | :---------------: | :-------------------: | :----------------: | :-----------: | :---------: | :-------------: | :------------: |")
for puzzle in players_puzzles:
    puzzle_name = puzzle[0]
    puzzle_solution = ""
    if puzzle_name in db:
        n = db.get(puzzle_name,'')

        if type(n) == list:
            puzzle_solution = f"[Source Code]({n[0]})<br><br>[Solution]({n[1]})"
        else:
            puzzle_solution = f"[Solution]({db.get(puzzle_name,'')})"
    puzzle_difficulty = puzzle[-2]
    puzzle_name = f"[{puzzle_name}](https://www.codingame.com/training//{(puzzle_name.replace(' ','-')).replace(''','').lower()})"
    puzzle_attempts = puzzle[5]
    puzzle_success = puzzle[7]
    puzzle_rating = puzzle[8]+"⭐"
    puzzle_tags = puzzle[-1]
    puzzle = [puzzle_name, puzzle_difficulty, puzzle_attempts, puzzle_success, puzzle_rating, puzzle_tags, puzzle_solution]
    print(f"| {' | '.join(puzzle)}  | ✔️ |")

