# Hashmap for ordering the output.
order = {"Pinned"=>0, "Followed"=>1,"none"=>2}

# Array for the comments and a hashmap to store replies to comments.
replies = {}
comments = []

n = gets.to_i
prev = "---"
n.times do
  comment = gets.chomp
  if comment[0] != " "
    comments << comment.split("|")
    prev = comment  
  else
    if replies.has_key?(prev)
        replies[prev] << comment.split("|")
    else
        replies[prev] = [comment.split("|")]
    end
  end
end

# Use a custom sort and then print the comments and replies in the correct order.
comments = comments.sort_by{|a| [order[a[-1]], -a[2].to_i, -a[1].split(":")[0].to_i,-a[1].split(":")[1].to_i]}
comments.each do |comment|
    comment = comment.join("|")
    puts comment
    if replies.include?(comment)
        reps = replies[comment]
        reps = reps.sort_by{|a| [order[a[-1]], -a[2].to_i, -a[1].split(":")[0].to_i,-a[1].split(":")[1].to_i]}
        reps.each{|rep|puts rep.join("|")}
    end
end
