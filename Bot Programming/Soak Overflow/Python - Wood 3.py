import sys
import math

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
width, height = [int(i) for i in input().split()]
for i in range(height):
    inputs = input().split()
    for j in range(width):
        # x: X coordinate, 0 is left edge
        # y: Y coordinate, 0 is top edge
        x = int(inputs[3*j])
        y = int(inputs[3*j+1])
        tile_type = int(inputs[3*j+2])

# game loop
while True:
    
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

    # Remove dead agents.
    my_dead = set(my_agents.keys()) - my_agents_seen
    their_dead = set(their_agents.keys()) - their_agents_seen
    for idx in my_dead:
        del my_agents[idx]
    for idx in their_dead:
        del their_agents[idx]

    # Shoot the wettest agent.
    wettest = None
    for idx, agent in their_agents.items():
        if wettest is None:
            wettest = agent
        if agent.wetness > wettest.wetness:
            wettest = agent

    my_agent_count = int(input())  # Number of alive agents controlled by you
    for i in range(my_agent_count):
        print(f"SHOOT {wettest.id}")

        # One line per agent: <agentId>;<action1;action2;...> actions are "MOVE x y | SHOOT id | THROW x y | HUNKER_DOWN | MESSAGE text"
