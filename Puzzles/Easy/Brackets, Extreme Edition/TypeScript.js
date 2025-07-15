// Get expression.
const expression: string = readline();

// Declare required inputs.
const pairs = new Map();
pairs.set("}","{");
pairs.set("]","[");
pairs.set(")","(");
let stack = [];
let valid = true;

for (let i = 0; i < expression.length; i++){
    let char : string = expression[i]
    // If char not a bracket -> ({[ then move on to next character
    if (!["(", "[", "{", ")", "]", "}"].includes(char)) {
        continue;
    }
    // Check if char is a closing bracket or not.
    if (pairs.has(char)){
        // If no character on stack or top of stack doesn't pair with char
        // set valid to false and break loop.
        if (stack.length == 0 || stack.pop() !== pairs.get(char)){
            valid = false;
            break;
        }
    }
    else{
        // Add open bracket to the stack.
        stack.push(char);
    }
}

// Output true if valid otherwise false
if (stack.length != 0){
    valid = false;
}
if (valid){
    console.log("true");
}else{
    console.log("false");
}
