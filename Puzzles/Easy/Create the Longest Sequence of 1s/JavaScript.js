// Get input value.
const b = readline();

// Split the array on 1s.
var arr = b.split("0");

// Get max size of two adjacent sets of 1s.
var max_size = 0;
var size;
for (let i = 0; i<arr.length-1;i++){
    size = arr[i].length + arr[i+1].length;
    if (size > max_size){
        max_size = arr[i].length + arr[i+1].length;
    }
}

// Return output + 1 for the flip bit.
console.log(max_size + 1);
