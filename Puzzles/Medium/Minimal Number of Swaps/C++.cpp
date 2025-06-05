#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    // Form Grid.
    int n;
    cin >> n; cin.ignore();
    int grid[n];
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x; cin.ignore();
        grid[i] = x;
    }

    // Swaps left most 0 with right most 1 until R < L.
    int swaps = 0;
    int l = 0;
    int r = n-1;
    while (l < r){
        while (l < r && grid[l] != 0){
            l += 1;
        }
        while (l < r && grid[r] != 1){
            r -= 1;
        }
        
        if (l < r){
            swaps += 1;
            l += 1;
            r -= 1;
        }
    }
    // Print the number of swaps required.
    cout << swaps << endl;
}
