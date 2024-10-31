#include <iostream>
#include <vector>
using namespace std;

int main()
{
    // Get inputs.
    int l;
    cin >> l; cin.ignore();
    int n;
    cin >> n; cin.ignore();

    vector<int> arr; 

    // Form array of bot positions.
    for (int i = 0; i < n; i++) {
        int b;
        cin >> b; cin.ignore();
        arr.push_back(b);
    }

    // Max time is for a furthest box from the end to reach the end.
    sort(arr.begin(),arr.end());
    double max = *std::max_element(arr.begin(), arr.end());
    double min = *std::min_element(arr.begin(), arr.end());
    if (l-min > max){
        cout << l-min << endl;
    }else{
        cout << max << endl;
    }
}

