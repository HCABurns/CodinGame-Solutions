# Get inputs list.
crazylist = gets.chomp.split.map(&:to_i)

# Find the difference between them.
a = crazylist[0,crazylist.size-1].zip(crazylist[1,crazylist.size-1]).map{|i,j| j-i}

if a.size > 1 and a[0] != a[1] then
    # Multiplication sequence. 
    d = a[1] / a[0].to_f
    puts (crazylist[-1] + a[-1]*d).to_i
else
    # Add/Subtract - a+(n)*d
    puts (crazylist[0] + (crazylist.size)*a[0])
end
