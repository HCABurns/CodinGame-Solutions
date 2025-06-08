class Node
  def initialize(name)
    @name = name
    @children = []
  end

  def name
    @name
  end

  def children
    @children
  end

  def add_child(child)
    @children << child
  end
end

#Get actor name and ensure it's not Kevin Bacon otherwise print 0 and quit.
actor_name = gets.chomp
if actor_name=="Kevin Bacon"
  print(0)
  exit()
end 

#Get number of films
n = gets.to_i
#Hashmap containing - String:Node
actors = {}

#Form Graph - Each Node is an actor - Each node has children relating to actors in the same films
n.times do
  movie, movie_cast = gets.chomp.split ":"
  movie_cast = movie_cast.strip.split ", "
  movie_cast.each do |cast|
    if actors.include?(cast) == false
      actors[cast] = Node.new(cast)
    end
    movie_cast.each do |c|
      actors[cast].add_child(c) if c != cast
    end
  end
end

#Find Kevin Bacon via BFS from the starting actor
links = 1
to_visit = actors[actor_name].children
while to_visit do
  if to_visit.include?("Kevin Bacon")
    puts links
    break
  else
    links += 1
    tmp = []
    to_visit.each do |name|
      actors[name].children.each do |actor_name|
        tmp << actor_name
      end
    end
    to_visit = tmp
  end
end
