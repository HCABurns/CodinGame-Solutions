// Get number of temperatures.
const n = parseInt(readline()); // the number of temperatures to analyse


// Define closest variable: If size is 0 don't set closest so the output will be 0.
var closest = 0;
if (n!=0){
    closest = 9999;
}

// Go thorugh each value and compare with closest. If it is smaller than closest, set new closest.
// If equal with closest then select the positive value if available.
var inputs = readline().split(' ');
for (let i = 0; i < n; i++) {
    const t = parseInt(inputs[i]);
    if (Math.abs(t) <= Math.abs(closest)){
        if (Math.abs(t) == Math.abs(closest) && !(t<0 && closest<0)){
            closest = Math.abs(closest);
        }else{
            closest = t;
        }
    }
}

// Output the closest value to 0.
console.log(closest);
