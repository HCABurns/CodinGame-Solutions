#include <iostream>
#include <vector>
using namespace std;

int main()
{
    // Define variables
    int n;
    vector<int> arr{};

    // Get inputs
    cin >> n; cin.ignore();
    for (int i = 0; i < n; i++) {
        int pi;
        cin >> pi; cin.ignore();
        arr.push_back(pi);
    }
    // Sort array
    sort(arr.begin(), arr.end());

    //Define difference
    int difference = 99999999;
    
    // Check adjacent horses power and store minimum difference.
    for (int i = 0; i < arr.size()-1; i++) {
        int val = arr.at(i+1) - arr.at(i);
        if (val < difference){
            difference = val;
        }
    }
    // Output the min difference
    cout << difference << endl;
}
