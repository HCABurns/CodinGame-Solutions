read -r n

if [ $n -eq 1 ]; then
    echo "1"
else
    echo $((6*(n-2)*(n-2) + 12 * (n-2) + 8))
fi
