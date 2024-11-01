//   Get values to be used to find GCD.
var inputs = readline().split(' ');
var a = parseInt(inputs[0]);
var b = parseInt(inputs[1]);
const a_start = a, b_start = b;


// Continue until remainder is 0.
while (b !== 0) {
    console.log(`${a}=${b}*${Math.floor(a/b)}+${a%b}`);
    var tmp = a%b;
    a = b;
    b = tmp;
}

// Output the GCD of a and b.
console.log(`GCD(${a_start},${b_start})=${a}`);
