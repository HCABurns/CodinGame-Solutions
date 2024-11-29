import random

MIN_RATE = 99
MAX_RATE = 100

MIN_VAL = 990
MAX_VAL = 999

def create_pair():
    value = random.randint(MIN_VAL,MAX_VAL)
    rate = random.randint(MIN_RATE,MAX_RATE)
    return value, rate

resource_amount = 1401
print(resource_amount)
for i in range(resource_amount):
    print(*create_pair())
