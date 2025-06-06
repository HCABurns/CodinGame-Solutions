# Get values.
read -r n
read -r -a myArray
grid=()
for (( i=0; i<$n; i++ )); do
    x=${myArray[$((i))]}
    grid+=(${myArray[$((i))]})
done

# Swaps left most 0 with right most 1 until R < L.
swaps=0
l=0
r=$((n - 1))
while [ "$l" -lt "$r" ]; do
    while [ "$l" -lt "$r" ] && [ "${grid[$l]}" != "0" ]; do
        ((l++))
    done
    while [ "$l" -lt "$r" ] && [ "${grid[$r]}" != "1" ]; do
        ((r--))
    done

    if [ "$l" -lt "$r" ]; then
        ((swaps++))
        ((l++))
        ((r--))
    fi
done

# Print the number of swaps required.
echo "$swaps"
