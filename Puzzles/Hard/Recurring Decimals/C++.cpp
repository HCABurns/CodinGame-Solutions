#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
int main()
{   
    // Get the value and set the remainder.
    int n;
    cin >> n; cin.ignore();
    int remainder = 1;

    // Array for storing ints, hashmap for storing index and index.
    string res = "";
    int idx = 0;
    unordered_map<int, int> values = {};

    // Complete the divison until terminates or repeat found.
    while (remainder != 0){
        // Check for repeated remainder.
        if (values.contains(remainder)){
            string left = res.substr(0,values[remainder]);
            string right = res.substr(values[remainder],res.size());
            res = left + "(" + right + ")";
            break;
        }
        values[remainder] = idx;

        // Complete the division.
        remainder *= 10;
        int val = remainder / n;
        res += std::to_string(val);
        remainder = remainder % n;
        
        // Increment index variable.
        idx += 1;
    }
    // Print the value.
    cout << "0." << res << endl;
}
