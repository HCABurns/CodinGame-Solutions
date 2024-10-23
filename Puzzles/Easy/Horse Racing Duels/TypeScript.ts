// Get size of inputs and store in a array.
const N: number = parseInt(readline());
let nums: number[] = [];
for (let i = 0; i < N; i++) {
    const pi: number = parseInt(readline());
    nums.push(pi);
}

// Sort array.
nums = nums.sort((n1,n2) => n1 - n2);

// Define difference variable.
let maxVal: number = 10000001;

// Check adjacent horses power and store minimum difference.
for (let i = 0;i<N-1;i++){
    if ((nums.at(i+1)-nums.at(i))<maxVal){
        maxVal = nums.at(i+1)-nums.at(i);
    }
}
//Output minimum distance
console.log(maxVal);
