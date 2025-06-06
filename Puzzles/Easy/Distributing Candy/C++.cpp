#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{   
    // Read in sweets and form array.
    int n;
    int m;
    cin >> n >> m; cin.ignore();
    int sweets[n];
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x; cin.ignore();
        sweets[i] = x;
    }

    // Sort array.
    int val = sizeof(sweets) / sizeof(sweets[0]);
    sort(sweets, sweets+val);

    // Find the minimum difference.
    int minDifference = 999;
    for (int i = 0; i < n-m+1; i++) {
        minDifference = min(sweets[i+m-1] - sweets[i] , minDifference);
    }

    // Print the minimum difference.
    cout << minDifference << endl;
}
