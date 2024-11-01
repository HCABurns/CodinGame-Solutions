#include <iostream>
using namespace std;

int main()
{
    //  Get values to be used to find GCD.
    int a;
    int b;
    cin >> a >> b; cin.ignore();
    int a_start = a;
    int b_start = b;

    // Continue until remainder is 0.
    while (b != 0){
        cout << a << "=" << b << "*" << (a/b) << "+" << (a%b) << endl;
        int tmp = a%b;
        a = b;
        b = tmp;
    }

    //  Output the GCD of a and b.
    cout << "GCD(" << a_start << "," << b_start << ")=" << a << endl;
}
