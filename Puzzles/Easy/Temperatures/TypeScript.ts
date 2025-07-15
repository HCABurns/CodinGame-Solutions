const n: number = parseInt(readline()); // the number of temperatures to analyse
var inputs: string[] = readline().split(' ');

var temp: number = -99999;

for (let i = 0; i < n; i++) {
    const t: number = parseInt(inputs[i]);// a temperature expressed as an integer ranging from -273 to 5526

    // Find temp closest to 0 and prioritise positive over negatives if equal.
    if (Math.abs(t) <= Math.abs(temp)){
        if (Math.abs(t) < Math.abs(temp)){
            temp = t;
        }else{
            if (t > temp){
                temp = t;
            }
        }

    }

}

// Print the closest to zero.
if (temp != -99999){console.log(temp);}
else{console.log(0)}
