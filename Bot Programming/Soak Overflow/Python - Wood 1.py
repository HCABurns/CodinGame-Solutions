import sys
import math
from collections import deque
from collections import defaultdict

# Class for storing information about a Agent.
class Agent:
    def __init__(self,shoot_cooldown, optimal_range, soaking_power, splash_bombs, ID):
        self.id = ID
        self.x = 0
        self.y = 0
        self.shoot_cooldown = shoot_cooldown
        self.optimal_range = optimal_range
        self.soaking_power = soaking_power
        self.splash_bombs = splash_bombs
        self.wetness = 0

    def update(self, x, y, cooldown, splash_bombs, wetness):
        self.x = x
        self.y = y
        self.shoot_cooldown = cooldown
        self.splash_bombs = splash_bombs
        self.wetness = wetness


# Function to find the closest cover
def bfs(goal, x, y):
    visited  = set((y,x))
    queue = deque([[y,x]])
    
    while queue:
        y, x = queue.popleft()
        
        print(y,x , goal , file = sys.stderr)
        if grid[y][x] == goal:
            return [y,x]
        
        for dy,dx in [[0,1],[1,0],[-1,0],[0,-1]]:
            if 0 <= dy+y < height and 0 <= dx+x<width and (dy+y,dx+x) not in visited:
                queue.append([dy+y,dx+x])
                visited.add((dy+y,dx+x))
    return [-999,-999]

def manhattan(y,x,i,j):
    return abs(y-i) + abs(x-j)


def is_shootable(y,x,i,j):
    if y == i and x > j:
        if grid[y][x-1] != 0 or grid[i][j+1] != 0:
            return False
    elif y == i and x < j:
        if grid[y][x+1] != 0 or grid[i][j-1] != 0:
            return False
    return True

# Form Hashmap of agents.
my_agents = {}
their_agents = {}
my_id = int(input())  # Your player id (0 or 1)
agent_data_count = int(input())  # Total number of agents in the game
for i in range(agent_data_count):
    # agent_id: Unique identifier for this agent
    # player: Player id of this agent
    # shoot_cooldown: Number of turns between each of this agent's shots
    # optimal_range: Maximum manhattan distance for greatest damage output
    # soaking_power: Damage output within optimal conditions
    # splash_bombs: Number of splash bombs this can throw this game
    agent_id, player, shoot_cooldown, optimal_range, soaking_power, splash_bombs = [int(j) for j in input().split()]
    if player == my_id:
        my_agents[agent_id] = Agent(shoot_cooldown, optimal_range, soaking_power, splash_bombs, agent_id)
    else:
        their_agents[agent_id] = Agent(shoot_cooldown, optimal_range, soaking_power, splash_bombs, agent_id)


## Read in information regarding the map.
# width: Width of the game map
# height: Height of the game map
grid = []
width, height = [int(i) for i in input().split()]
for i in range(height):
    inputs = input().split()
    grid += [[]]
    for j in range(width):
        # x: X coordinate, 0 is left edge
        # y: Y coordinate, 0 is top edge
        x = int(inputs[3*j])
        y = int(inputs[3*j+1])
        tile_type = int(inputs[3*j+2])
        grid[-1].append(tile_type)

print("Map read in" , file = sys.stderr)

pos = 0
stuck_agent = 0
# game loop
while True:
    print("Loop started" , file = sys.stderr)
    actions = defaultdict(list)

    ## Get agents in the game still and update their values.
    agent_count = int(input())  # Total number of agents still in the game
    my_agents_seen = set()
    their_agents_seen = set()
    for i in range(agent_count):
        # cooldown: Number of turns before this agent can shoot
        # wetness: Damage (0-100) this agent has taken
        agent_id, x, y, cooldown, splash_bombs, wetness = [int(j) for j in input().split()]
        if agent_id in my_agents:
            my_agents[agent_id].update(x, y, cooldown, splash_bombs, wetness)
            my_agents_seen.add(agent_id)
        else:
            their_agents[agent_id].update(x, y, cooldown, splash_bombs, wetness)
            their_agents_seen.add(agent_id)
    
    print("Agents in" , file = sys.stderr)

    # Remove dead agents.
    my_dead = set(my_agents.keys()) - my_agents_seen
    their_dead = set(their_agents.keys()) - their_agents_seen
    for idx in my_dead:
        del my_agents[idx]
    for idx in their_dead:
        del their_agents[idx]
    print("dead gone" , file = sys.stderr)

    """
    # Move to the closest enemy
    for agent_id in my_agents:
        my_x, my_y = my_agents[agent_id].x, my_agents[agent_id].y

        closest = None
        closest_dist = 9999
        for idx, agent in their_agents.items():
            dist = manhattan(my_y, my_x, agent.y, agent.x)
            #if dist < 3: closest = None; break
            # else:
            if dist < closest_dist:
                closest , closest_dist = agent, dist

        if closest:
            if closest_dist > 4:
                actions[agent_id].append(f"MOVE {my_x - (my_x - closest.x - 4)} {my_y}")
            if closest_dist <= 4:
                actions[agent_id].append(f"THROW {closest.x} {closest.y}")
    """
    """
    # Move to the highest cover
    for agent_id in my_agents:
        my_x, my_y = my_agents[agent_id].x, my_agents[agent_id].y
        
        if my_x == 0:
            if grid[my_y-1][my_x+1] == 2:
                actions[agent_id].append(f"MOVE {my_x} {my_y-1}")
            else:
                actions[agent_id].append(f"MOVE {my_x} {my_y+1}")
        else:
            if grid[my_y-1][my_x-1] == 2:
                actions[agent_id].append(f"MOVE {my_x} {my_y-1}")
            else:
                actions[agent_id].append(f"MOVE {my_x} {my_y+1}")

        ### This is for later
        closest_low = bfs(1,my_x,my_y)
        closest_high = bfs(2,my_x,my_y)
        print(closest_low, closest_high , file = sys.stderr)
        if closest_high == closest_low == [-999,-999]:
            continue
        elif manhattan(*closest_high,my_y,my_x) <= manhattan(*closest_high,my_y,my_x) and closest_high != [-999,-999]:
            actions[agent_id].append(f"MOVE {closest_high[0]} {closest_high[1]}")
        elif manhattan(*closest_high,my_y,my_x) >= manhattan(*closest_high,my_y,my_x) and closest_low != [-999,-999]:
            actions[agent_id].append(f"MOVE {closest_low[0]} {closest_low[1]}")
        """

    
    # Shoot the wettest agent.
    """
    print("Find wettest" , file = sys.stderr)
    wettest = None
    for idx, agent in their_agents.items():
        if wettest is None:
            wettest = agent
        if agent.wetness > wettest.wetness:
            wettest = agent
    print("Found wettest agent" , file = sys.stderr)
    """

    """
    # Shoot the least protected
    protection = {}
    for idx, agent in their_agents.items():
        x = agent.x
        y = agent.y
        protection[idx] = sum([grid[y+i][x+j] for i,j in [[0,1],[1,0],[-1,0],[0,-1]]])
    print(protection , file = sys.stderr)
    """

    # Throw bomb at closest
    #for idx, agent in their_agents.items():pass


    my_agent_count = int(input())  # Number of alive agents controlled by you
    for i in range(my_agent_count):
        ##actions[i+1].append(f"SHOOT {wettest.id}")
        y , x = my_agents[i+1].y , my_agents[i+1].x
        
        """
        # Closest to agent with least protection:
        least = None
        for idx in their_agents:
            print(idx, file = sys.stderr)
            if least == None:
                least = their_agents[idx]
            else:
                if manhattan(their_agents[idx].y,their_agents[idx].x, y, x) <= manhattan(least.y,least.x, y, x):
                    if protection[least.id] >= protection[idx] and is_shootable(y,x,their_agents[idx].y,their_agents[idx].x):
                        least = their_agents[idx]
        """

        #actions[i+1].append(f"SHOOT {least.id}")
        #print(f"SHOOT {wettest.id}")

    print(actions, file = sys.stderr)
    for action in actions:
        print(str(action)+";"+";".join(actions[action]), file = sys.stderr)
        print(str(action)+";"+";".join(actions[action]))
        # One line per agent: <agentId>;<action1;action2;...> actions are "MOVE x y | SHOOT id | THROW x y | HUNKER_DOWN | MESSAGE text"

    # find the stuck agent
    # (15,12)
    if stuck_agent == 0:
        middle_agent = [0,0]
        if height % 2 == 0:
            middle_agent[1] = (height+1)//2
        else:
            middle_agent[1] = height//2
        if width % 2 == 0:
            middle_agent[0] =(width+1)//2
        else:
            middle_agent[0] = width//2 

        stuck_agent = 0
        for idx,agent in my_agents.items():
            print(middle_agent , [agent.x, agent.y] , file = sys.stderr)
            if [agent.x, agent.y] == middle_agent:
                middle_agent = idx
                stuck_agent = 1 if idx == 2 else 2



    # Find the segment of agent 2
    x = my_agents[stuck_agent].x
    y = my_agents[stuck_agent].y
    segment = 0
    if x < 6 and y < 6:
        segment = 0
    elif x > 6 and y < 6:
        segment = 1
    elif x < 6 and y > 5:
        segment = 2
    else:
        segment = 3

    moves = ["MOVE 6 2", f"MOVE {width-7} 2", "MOVE 6 9", f"MOVE {width-7} 9"]
    poss = [[6,2], [width-7,2], [6,9], [width-7,9]]
    throws = ["THROW 2 2", f"THROW {width-3} 2","THROW 2 9", f"THROW {width-3} 9"]

    if pos == segment:
        pos += 1

    if pos < 4:
        if poss[pos][0] != my_agents[middle_agent].x or poss[pos][1] != my_agents[middle_agent].y:
            print(f"{middle_agent};"+moves[pos])
        else:
            print(f"{middle_agent};"+throws[pos])
            pos += 1
    print(f"{stuck_agent};HUNKER_DOWN")
