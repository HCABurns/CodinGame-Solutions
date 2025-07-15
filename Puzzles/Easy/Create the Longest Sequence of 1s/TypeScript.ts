// Get input.
const b: string[] = readline().split("0");

// Find longest string of 1s.
let longest : number = 0;
for (let i = 0 ; i < b.length - 1; i++){

    if (b[i].length + b[i+1].length + 1> longest){
        longest = b[i].length + b[i+1].length  + 1;
    }

}

// Print the longest string of 1s.
console.log(longest);
