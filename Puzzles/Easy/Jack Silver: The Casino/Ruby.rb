# Get rounds amount and starting cash amount.
rounds = gets.to_i
cash = gets.to_i
rounds.times do
  # Get bet and remove from cash.
  bet_amount = (cash.to_f/4).ceil
  cash -= bet_amount

  # Get the play and get required variables.
  play = gets.chomp.split
  number = play[0].to_i
  bet = play[1]

  # Detemrine if bet it a win or loss. 
  if bet == "ODD"
    cash += bet_amount*2 if number % 2 == 1
  elsif bet == "EVEN"
    cash += bet_amount*2 if number != 0 && number % 2 == 0
  else
    cash += bet_amount * 36 if number == play[2].to_i
  end
end

# Print cash after playing.
puts cash
