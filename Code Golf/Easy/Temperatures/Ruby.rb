gets
p gets.split.map(&:to_i).max_by{|y|[y*-y,y]}.to_i
