# Get starting number.
n = gets.to_i+1

# Two variables to store primes.
p1 = nil
p2 = nil

# Continue until two primes that has a difference of 2 have been found.
while p2 == nil do
    # Find if n is a prime.
    is_prime = true
    (2..(Math.sqrt(n)+1)).each do |i|
      if n % i == 0
        is_prime = false
        break
      end
    end
    # If prime, increment by 2 othewise reset variables and increment by 1.
    if is_prime != false
      if p1 == nil
        p1 = n
        n+=2
      else
        p2 = n
      end
    else
      p1 = nil
      p2 = nil
      n+=1
    end
end

# Output the two primes with a difference of 2.
puts p1.to_s + " " + p2.to_s
