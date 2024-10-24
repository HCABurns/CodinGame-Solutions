-- Define variables
local difference = 10000000
local N = tonumber(io.read())
local arr = {}

-- Fill array with horse strength
for i = 1, N do
    arr[i] = tonumber(io.read())
end

-- Sort array
table.sort(arr)

-- Check adjacent horses power and store minimum difference
for i = 1, N - 1 do
    local val = arr[i + 1] - arr[i]
    if val < difference then
        difference = val
    end
end

-- Output the min difference
print(difference)
