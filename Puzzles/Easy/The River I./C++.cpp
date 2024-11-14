#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    // Get inputs.
    long long r_1;
    cin >> r_1; cin.ignore();
    long long r_2;
    cin >> r_2; cin.ignore();

    // Ensure r_1 is the smaller value.
    if (r_2 < r_1){
        long tmp = r_1;
        r_1 = r_2;
        r_2 = tmp;
    }

    // Continue until equal values.
    while (r_1 != r_2){
        // Compute algorithm until r_1 is larger or equal to r_2.
        while (r_1 < r_2){
            std::string r_1_str = std::to_string(r_1);
            for (char c : r_1_str){
                r_1 += (long)c - '0';
            }
        }
        
        // If r_2 is smaller than r_1, compute the next value.
        while (r_2 < r_1){
            std::string r_2_str = std::to_string(r_2);
            for (char c : r_2_str){
                r_2 +=(long)c - '0';
            }
        }

    }
    // Output the meeting point.
    cout << r_1 << endl;
}
