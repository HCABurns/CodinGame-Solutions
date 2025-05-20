// Define required variables.
const expression = readline();
var valid = true;
let stack = [];
let pairs = {};
pairs['}'] =  '{';
pairs[']'] =  '[';
pairs[')'] =  '(';
let str = "(){}[]"

// Iterate through chars and check char is valid, if opening add it to stack
// if closing then check if top of stack is a pair.
for (let i = 0; i < expression.length; i++){
    let c = expression.charAt(i);
    if (str.includes(c+"") == true){
        if (c in pairs){
            if (stack.length == 0 || stack.pop() != pairs[c]){
                valid = false;
            }
        }
        else{
            stack.push(c);
        }
    }
}

// Output true if valid otherwise false
if (stack.length == 0 && valid){
    console.log('true');
}else{
    console.log('false');
}
