#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n; // the number of temperatures to analyse
    cin >> n; cin.ignore();

    // Find temp closest to 0 and prioritise positive over negatives if equal.
    int temp = -999999;
    for (int i = 0; i < n; i++) {
        int t;
        cin >> t; cin.ignore();
        
        if (abs(t) < abs(temp)){
            temp = t;
        }else if (abs(t) == abs(temp)){
            temp = max(t,temp);
        }

    }

    // Print correct output.
    if (temp != -999999){
        cout << temp << endl;
    }else{
        cout << 0 << endl;
    }
}
