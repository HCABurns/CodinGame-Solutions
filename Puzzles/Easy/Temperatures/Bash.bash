# n: the number of temperatures to analyse
read -r n
read -r -a myArray

# Find temp closest to 0 and prioritise positive over negatives if equal.
temp=-999999
for (( i=0; i<$n; i++ )); do
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t=${myArray[$((i))]}

    if [ "${t/-/}" -lt "${temp/-/}" ]; then
        (( temp = t ))
    elif [ "${t/-/}" -eq "${temp/-/}" ]; then
        if [ $t -gt $temp ]; then
            (( temp = t ))
        fi
    fi
done

# Print correct output.
if [ "${temp/-/}" -eq "999999" ]; then
    (echo "0")
else
    ( echo ${temp} )
fi
