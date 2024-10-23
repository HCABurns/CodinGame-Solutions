// Get number of inputs and form array of those inputs
const N = parseInt(readline());
const arr = [];
for (let i = 0; i < N; i++) {
    const pi = parseInt(readline());
    arr[i] = pi;
}

// Sort array.
arr.sort(function(a, b){return a - b})

// Check adjacent horses power and store minimum difference.
let difference = 9999999;
for (let i = 0; i < N-1; i++) {
    let val = arr[i+1] - arr[i];
    if (val < difference){
        difference = val;
    }
}

// Output minimum difference.
console.log(difference);
