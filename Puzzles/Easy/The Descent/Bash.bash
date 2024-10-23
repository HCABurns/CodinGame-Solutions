# game loop
while true; do
    # Set required variables.
    declare -i max_v=0
    declare -i max_i=0

    # Find the index of the max height and store in max_index.
    for (( i=0; i<8; i++ )); do
        read -r mountainH
        if [[ $mountainH -gt $max_v ]]; then
            max_v=$mountainH
            max_i=i  
        fi
    done
    # Output the index of the mountain to fire on.
    echo $max_i 
done
