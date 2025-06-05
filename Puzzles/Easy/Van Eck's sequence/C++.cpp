#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

int main()
{
    // Get inputs.
    int a1;
    cin >> a1; cin.ignore();
    int n;
    cin >> n; cin.ignore();

    // Create map for storing indexes.
    std::unordered_map<int,int> map = {};
    
    // Complete sequence.
    for (int i = 0; i<n-1;i++){
        if (!map.contains(a1)){
            map[a1] =  i;
            a1 = 0;
        }else{
            int tmp = (i - map[a1]);
            map[a1] =  i;
            a1 = tmp;
        }
    }
    // Output the value.
    cout << a1 << endl;
}
