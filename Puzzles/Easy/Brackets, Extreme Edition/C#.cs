using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Solution
{
    static void Main(string[] args)
    {
        string expression = Console.ReadLine();

         // Declare required variables.
        Stack stack = new Stack();
        bool valid = true;
        Dictionary<char, char> pairs = new Dictionary<char, char>();
        pairs.Add(')','(');
        pairs.Add('}','{');
        pairs.Add(']','[');
        string v = "({[";
        

        for (int i = 0; i < expression.Length; i++){
            // If char not a bracket -> ({[ then move on to next character
            if (pairs.ContainsKey(expression[i]) || v.Contains(expression[i])){
                // Check if char is a closing bracket or not.
                if (pairs.ContainsKey(expression[i])){
                    // If no character on stack or top of stack doesn't pair with char
                    // set valid to false.
                    if (stack.Count == 0){valid = false;break;}
                    char popped = (char) stack.Pop();
                    if (pairs[expression[i]] != popped){
                        valid = false;
                    }
                }
                else{
                    // Append open bracket to the stack.
                    stack.Push(expression[i]);
                }
            }
        }
        // Output true if valid otherwise false
        if (valid && stack.Count == 0){
            Console.WriteLine("true");
        }
        else{
            Console.WriteLine("false");}
    }
}
