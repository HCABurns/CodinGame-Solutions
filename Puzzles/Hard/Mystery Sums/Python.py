# Get statment and split.
expression, res = input().split(" = ")
res = int(res.strip())

# Find ? locations and the set their values to be 0
unknown = [i for i in range(len(expression)) if expression[i] == "?"]
nums = [1 for _ in unknown]
expression = list(expression)
i = 0

if not nums:
    # No ? so print original statement.
    print("".join(expression),"=",res)

# Find the correct expression.
while nums:
    while nums[i] < 10:
        
        for pos,idx in enumerate(unknown):
            expression[idx] = str(nums[pos])
        try:
            if eval("".join(expression)) == res:
                print("".join(expression),'=',res)
                nums = []
                break
        except:
            continue
        nums[i]+=1
    
    if nums:
        nums[(i+1) % len(nums)] += 1
        nums[0] = 1
