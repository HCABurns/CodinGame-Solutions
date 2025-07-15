// Get inputs.
const MESSAGE: string = readline();
let h : string[] = ["00","0"]
let b : string =""

// Convert to 7 bit binary.
for (let i = 0; i < MESSAGE.length; i++){
    b += MESSAGE.charCodeAt(i).toString(2).padStart(7, '0');
}

let previous = '0';
// Iterate over binary string and add correct value to array.
for (let i = 0;  i < b.length; i++){
    // If first value or current value is not equal to the previous (i.e previous was 1 and val is 0) add correct identifier.
    if (i==0 || b[i]!=previous){
        previous=b[i]
        h.push(h[parseInt(previous,10)])
        h.push("")
    }
    
    // Increment count by 1
    h[h.length-1] += "0"
}

// Output the correct
console.log(h.slice(2,h.length).join(" "))
