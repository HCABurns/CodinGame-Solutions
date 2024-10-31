// Get inputs.
const L = parseInt(readline());
const N = parseInt(readline());
var inputs = readline().split(' ');

// Form array of bots postitions.
const arr = [];
for (let i = 0; i < N; i++) {
    const b = parseInt(inputs[i]);
    arr[i] = b;
}

// Max time is for a furthest box from the end to reach the end.
arr.sort(function(a, b){return a - b})
console.log(Math.max(L-arr[0] , arr[N-1]));
