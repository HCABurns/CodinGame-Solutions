# Define hashmaps to be used.
beats = {"Scissors"=>"Paper","Paper"=>"Rock","Rock"=>"Scissors"}
loses = {"Scissors"=>"Rock","Rock"=>"Paper","Paper"=>"Scissors"}

# Get all players choices and store in array.
n = gets.to_i
players = []
n.times do
  players << gets.chomp
end

# Find the best choice and starting position to win the most without losing once.
max_winning = 0
max_selection = ["",0]
(0..n-1).each do |i|
  first_opponent_idx = (i+1)%n
  wins = 1
  player_selection = loses[players[first_opponent_idx]]
  (0..n-2).each do |j|
    if beats[player_selection] == players[(first_opponent_idx+j)%n]
      wins+=1
    elsif loses[player_selection] == players[(first_opponent_idx+j)%n]
      break
    end
  end
  # Set new max is more wins than previous max.
  if wins > max_winning
    max_winning = wins
    max_selection = [player_selection,first_opponent_idx]
  end
end

# Output choice and first opponent id.
puts max_selection[0]
p max_selection[1]
