declare -a arr=()
read -r N
for (( i=0; i<$N; i++ )); do
    read -r Pi
    arr+=($Pi)
done

# Define max valuable variable
declare -i maxVal=9999999
# Sort horses in order of strength
IFS=$'\n' sorted=($(sort -n <<<"${arr[*]}"))
unset IFS

# Compare adjacent horses and store the minimum value between them
for (( i=0; i<$N-1; i++ )); do
    declare -i num1="$((${sorted[i+1]}-${sorted[i]}))"
    if [[ $num1 -lt $maxVal ]]; then
        maxVal=$num1
    fi
done
#Print output
echo $maxVal
