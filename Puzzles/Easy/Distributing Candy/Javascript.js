// Get sweets and form array.
var inputs = readline().split(' ');
const n = parseInt(inputs[0]);
const m = parseInt(inputs[1]);
let sweets = [];
var inputs = readline().split(' ');
for (let i = 0; i < n; i++) {
    const x = parseInt(inputs[i]);
    sweets[i]=x;
}

// Sort array.
sweets.sort(function(a, b){return a - b})

// Get minimum difference between m bags.
let minDifference = 999;
for (let i = 0; i < n-m+1; i++) {
    minDifference = Math.min(sweets[i+m-1] - sweets[i], minDifference);
}

// Output minimum difference between m sweet bags.
console.log(minDifference);
