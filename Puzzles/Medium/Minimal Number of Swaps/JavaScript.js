// Form Grid.
const n = parseInt(readline());
var inputs = readline().split(' ');
var grid = [];
for (let i = 0; i < n; i++) {
    const x = parseInt(inputs[i]);
    grid[i] = x;
}

// Swaps left most 0 with right most 1 until R < L.
var swaps = 0;
var l = 0;
var r = n-1;
while (l < r){
    while (l < r && grid[l] != 0){
        l += 1;
    }
    while (l < r && grid[r] != 1){
        r -= 1;
    }
    
    if (l < r){
        swaps += 1;
        l += 1;
        r -= 1;
    }
}
// Print the number of swaps required.
console.log(swaps);
