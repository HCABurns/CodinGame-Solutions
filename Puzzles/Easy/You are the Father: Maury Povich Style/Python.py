def get_chromosomes(str , idx):
    """
    Helper function to extract chromosomes pairs from the input string.

    Parameters:
    str - String to be extracted from
    idx - The id of the first : character. Used to split between name and chromosomes.

    Return - Array of strings of pairs of chromosomes.
    """
    return str[idx+1:].lstrip().split(" ")

# Get mothers chromosomes pairs.
mother = input()
mothers_chromosomes = get_chromosomes(mother, mother.find(":"))

#Get childs chromosomes pairs.
child = input()
child_chromosomes = get_chromosomes(child, child.find(":"))

# Find the chromosomes given from the father or both if indistinguishable from mothers.
to_find = []
for i,j in zip(child_chromosomes, mothers_chromosomes):
    if i == j or i[::-1]==j:
        to_find.append(i)
        continue
    for k in i:
        if i.count(k) == 2:
            to_find.append(k);break
        elif k not in j:
            to_find.append(k);break

# Check for father. All of to_find will be in the fathers chromosomes. 
num_of_possible_fathers = int(input())
for i in range(num_of_possible_fathers):
    # Split father string and get name and chromosomes.
    possible_father = input()
    split_idx = possible_father.find(":")
    father_name = possible_father[:split_idx]
    chromosomes = get_chromosomes(possible_father, split_idx)
    valid = True

    # Check all pairs and break if not compatible.
    for child,father in zip(to_find, chromosomes):
        if len(child) == 2:
            if child[0] not in father and child[1] not in father:
                valid = False
                break
        else:
            if child not in father:
                valid = False
                break
    # If still valid, break the loop and print.
    if valid:
        break

# Output name of father of the child.
print(f"{father_name}, you are the father!")
