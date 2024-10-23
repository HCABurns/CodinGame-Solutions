# Get required inputs
inputs = {}
swapper = {"_":'0',"-":'1'}
reverse_swapper = {"0":"_","1":"-"}
n = int(input())
m = int(input())
# Get inputs and convert to 1 or 0 using the swapper.
for i in range(n):
    input_name, input_signal = input().split()
    o = ""
    for i in input_signal:
        o+=swapper[i]
    inputs[input_name] = o

# Go through the required outputs and perfrom the correct operation.
for i in range(m):
    output_name, _type, i1, i2 = input().split()
    out = ""
    val = ""
    if _type == "AND":
        val = [i if i==j else "0" for i,j in zip(inputs[i1],inputs[i2]) ]
    elif _type == "OR":
        val = [int(i) or int(j) for i,j in zip(inputs[i1],inputs[i2])]
    elif _type=="XOR":
        val = [int(i)^int(j) for i,j in zip(inputs[i1],inputs[i2])]
    elif _type=="NAND":
        val = ["0" if (int(i) and int(j)) else "1"  for i,j in zip(inputs[i1],inputs[i2]) ]
    elif _type=="NOR":
        val = ["0" if int(i) or int(j) else "1" for i,j in zip(inputs[i1],inputs[i2])]
    elif _type=="NXOR":
        val = ["1" if int(i)==int(j) else "0" for i,j in zip(inputs[i1],inputs[i2])]

    #Convert back into required from and output result
    out = "".join([reverse_swapper[str(i)] for i in val])
    print(f"{output_name} {out}")
