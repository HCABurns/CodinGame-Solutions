// Get the value and set the remainder.
const n = parseInt(readline());
var remainder = 1;

// Array for storing ints, hashmap for storing index and index.
var res = "";
var idx = 0;
var values = {};

// Complete the divison until terminates or repeat found.
while (remainder != 0){
    // Check for repeated remainder.
    if (remainder in values){
        let recurring = res.slice(values[remainder]);
        res = res.slice(0,values[remainder]) + "(" + recurring + ")";
        break;
    }
    values[remainder] = idx

    // Complete the division.
    remainder *= 10;
    var val = Math.floor(remainder / n);
    res += val.toString()
    remainder = remainder % n;

    // Increment index variable.
    idx += 1;
}

// Print the value.
console.log("0." + res);
