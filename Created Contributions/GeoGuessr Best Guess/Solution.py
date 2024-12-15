# Get information from photo.
info = input().split(":")

# Get number of candidates.
n = int(input())

# Create hashmap of int:string (Matches # : country name)
# Ignore if matches # already in hashmap. (Satisfy tiebreak rule)
matching_information = {}
for i in range(n):
    country, *knowledge = input().split(":")
    matches = sum([1 for i in knowledge if i in info])
    if matches not in matching_information:
        matching_information[matches] = country
      
# Print best guess otherwise 'No Guess'.
best_guess = max(matching_information.items())
if best_guess[0] != 0:
    print(best_guess[1])
else:
    print("No guess")
