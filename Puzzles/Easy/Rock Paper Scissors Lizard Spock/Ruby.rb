# Define array of players. [ID, sign, array of who they beat]
arr = []
n = gets.to_i
n.times do
  numplayer, signplayer = gets.split
  numplayer = numplayer.to_i
  arr << [numplayer, signplayer, []]
end

#Hashmap of which options beat others.
hashmap = { "C" => "PL", "R" => "LC", "P" => "RS", "L" => "PS", "S" => "RC" }

# Run Simuation
while arr.size > 1 do
  (arr.size / 2).times do |i|
    p1 = arr[i]
    p2 = arr[i+1]

    # Determine the winner.
    if p1[1] == p2[1]
      if p1[0] < p2[0]
        to_remove = p2
      else
        to_remove = p1
      end
    elsif hashmap[p1[1]].include?(p2[1])
      to_remove = p2
    else
      to_remove = p1
    end
    
    # Remove player who lost.
    arr.delete(to_remove)

    # Append losers id to the winners 'beat' list.
    if to_remove == p1
      p2[2].push(p1[0])
    else
      p1[2].push(p2[0])
    end
  end
end

# Output the winners id and the ids of the players that they beat.
p arr[0][0]
puts arr[0][2].join(" ")
