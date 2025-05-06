-- Get number of temperatures to analyse.
n = tonumber(io.read())

-- Populate array with temperatures.
arr = {}
next_token = string.gmatch(io.read(), "[^%s]+")
for i=1,n do
    t = tonumber(next_token())
    arr[i] = {t*-t, t}
end

-- Sort array based on closest to zero. (Prefer pos over negative if equal)
table.sort(arr, function(a, b)
    if math.abs(a[1]) == math.abs(b[1]) then
        return a[2] > b[2]
    else
        return math.abs(a[1]) < math.abs(b[1])
    end
end)

-- Print the output.
if n == 0 then
    print(0)
else
    print(arr[1][2])
end
