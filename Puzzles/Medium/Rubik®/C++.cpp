#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n; cin.ignore();

    if (n == 1){
        cout << "1" << endl;
    }else{
        cout << (6*(n-2)*(n-2) + 12 * (n-2) + 8) << endl;
    }
}
