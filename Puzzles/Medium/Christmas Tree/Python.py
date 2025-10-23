n = int(input())-1
i = int(input())

h = int((-(2 - i) + ((2 - i)**2 + 8*i*n)**0.5) // (2*i))

sum_h = h * (2 + (h - 1) * i) // 2
remaining = n - sum_h
print(h + remaining + 1)
