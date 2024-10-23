class Node:
    """
    This holds information regarding a person and their "children". Children are actors in films with the actor.

    Methods:
    __init__(name) - Initialise a Node object with name string.
    get_name() - Returns string of name of the actor.
    get_children() - Returns array of strings of the actors in films with the actor.
    """
    def __init__(self,name):
        self.name = name
        self.children = []
    
    def get_name(self):
        return self.name

    def get_children(self):
        return self.children

#Get actor name and ensure it's not Kevin Bacon otherwise print 0 and quit.
actor_name = input()
if actor_name=="Kevin Bacon":print(0);quit()

#Get number of films
n = int(input())
#Hashmap containing - String:Node
actors = {}

#Form Graph - Each Node is an actor - Each node has children relating to actors in the same films
for i in range(n):
    movie , movie_cast = input().split(":")
    movie_cast = movie_cast.strip().split(", ")

    for cast in movie_cast:
        if cast not in actors:
            actors[cast] = Node(cast)
        actors[cast].children += [c for c in movie_cast if c!=cast]

#Find Kevin Bacon via BFS from the starting actor
links = 1
to_visit = actors[actor_name].get_children()
while to_visit:
    if "Kevin Bacon" in to_visit:
        print(links)
        break
    else:
        links+=1
        tmp = []
        for name in to_visit:
            for actor_name in actors[name].get_children():
                tmp.append(actor_name)
        to_visit = tmp
