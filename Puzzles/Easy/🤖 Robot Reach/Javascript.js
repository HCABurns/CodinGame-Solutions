// Get inputs.
const HEIGHT = parseInt(readline());
const WIDTH = parseInt(readline());
const THRESHOLD = parseInt(readline());

// Create visited array.
var visited = []

// Function to map string to int.
function charToInteger(char) {
    return "0123456789".indexOf(char);
  }

// Check each position and ensure value is below threshold and the cell is reachable from other valid cells.
for (let i = 0; i<HEIGHT;i++){
    for (let j = 0; j < WIDTH; j++){
        if (i==0 || visited.includes((i-1)+" "+j) || visited.includes(i+" "+(j-1))){
            var digits = (i.toString()+j.toString()).split("").map(charToInteger);
            var sum_val = 0;
            digits.forEach((val) => sum_val += val);
            if (sum_val <= THRESHOLD){
                visited.push(i+" "+j);
            }
        }
    }
}

// Print number of valid cells.
console.log(visited.length);
