-- game loop
while true do
    -- Declare required variables.
    max_v = 0
    max_i =0

    -- Find the index of the max height and store in max_i.
    for i=0,8-1 do
        mountainH = tonumber(io.read()) 
        if mountainH > max_v then
            max_v = mountainH
            max_i = i
        end
    end
    -- Output the index of the mountain to fire on.
    print(max_i)
end
