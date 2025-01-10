#include <iostream>
#include <string>
#include <stack>
#include <map>
using namespace std;

int main()
{
    // Get expression.
    string expression;
    cin >> expression; cin.ignore();

    // Declare required variables.
    stack<char> stack;
    bool valid = true;
    map<char, char> pairs = {{')','('},{']','['},{'}','{'}};
    string v = "({[";

    for (int i = 0; i < expression.length(); i++){
        // If char not a bracket -> ({[ then move on to next character
        if (pairs.contains(expression[i]) || v.find(expression[i]) < 3){
            // Check if char is a closing bracket or not.
            if (pairs.contains(expression[i])){
                // If no character on stack or top of stack doesn't pair with char
                // set valid to false.
                if (stack.size() == 0){valid = false;break;}
                char popped = stack.top();
                stack.pop();
                if (pairs[expression[i]] != popped){
                    valid = false;
                }
            }
            else{
                 // Append open bracket to the stack.
                stack.push(expression[i]);
            }
        }

    }
    // Output true if valid otherwise false
    if (valid && stack.empty()){
        cout << "true" << endl;
    }
    else{
        cout << "false" << endl;
    }
}
