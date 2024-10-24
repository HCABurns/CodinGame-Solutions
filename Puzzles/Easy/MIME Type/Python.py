# Get required inputs.
n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

hashmap = {}

# Store extention and mime type in hashmap
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    if ext not in hashmap:
        hashmap[ext.upper()] = mt

# Go through files to be analyzed and covert using hashamp.
for i in range(q):
    fname = input() 
    split = fname.split(".")
    if len(split)!=1:
        if hashmap.get(split[-1].upper(),None):
            if hashmap.get(split[-1].upper(),None):
                print(hashmap[split[-1].upper()])
        else:
            print("UNKNOWN")
    else:
        print("UNKNOWN")
