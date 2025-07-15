const L: number = parseInt(readline());
const H: number = parseInt(readline());
const T: string = readline().toUpperCase();
for (let i = 0; i < H; i++) {
    // Get ascii art row.
    const ROW: string = readline();
    var out : string = "";
    for (let i = 0; i < T.length; i++) {
        // Convert character to ordinal and minus value of "A".
        var j: number = T.charCodeAt(i)-65;
        
        //If J is less than 0 - It's a special character so convert to 26 (end of input)
        if (j<0){
            j=26;
        }

        // Multiply by the width to get to the correct position
        j=j*L;

        // Output correct character, no newline.
        out += ROW.slice(j,j+L);
    }
    // Print the ASCII ART row.
    console.log(out);
}
