# Hashmap for storing nodes.
nodes = {}

# Get inputs.
n = gets.to_i
v = gets.to_i
m = gets.to_i
m.times do
  parent, l, r = gets.split.map { |x| x.to_i }
  # Add node if not seen yet.
  nodes[parent] = [parent,nil,nil] if !nodes.key?(parent)
  nodes[l] = [l,nodes[parent],"Left"] if !nodes.key?(l)
  nodes[r] = [r,nodes[parent],"Right"] if !nodes.key?(r)
end

# Get route from node to root.
out = []
while nodes[v][1] != nil
    out << [nodes[v][2]]
    v = nodes[v][1][0]
end

# Print route from root to node or "Root" if root node.
puts out != [] ? out.reverse.join(" ") : "Root"
