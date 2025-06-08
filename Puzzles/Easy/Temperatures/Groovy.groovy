input = new Scanner(System.in);

// Find temp closest to 0 and prioritise positive over negatives if equal.
temp = 999999
n = input.nextInt() // the number of temperatures to analyse
for (i = 0; i < n; ++i) {
    t = input.nextInt() // a temperature expressed as an integer ranging from -273 to 5526

    if (Math.abs(t) < Math.abs(temp)){
        temp = t
    }
    else if (Math.abs(t) == Math.abs(temp)){
        temp = Math.max(temp, t)
    }

}

// Print the smallest temp.
if (temp != 999999){
    println temp
}else{
    println "0"
}
