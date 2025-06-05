#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main()
{
    float side;
    float diameter;
    cin >> side >> diameter; cin.ignore();

    // Calculate wasteful bakers amount.
    int wasteful = (int) pow(floor(side / diameter),2);
        
    // Calculate frugal bakers amount.
    int frugal = 0;
    double area = side*side;
    while (side > diameter){
        // Calculate amount possible to be cut.
        int amount = (int) floor(side / diameter);
        amount *= amount;
        // Convert wasted into a new dough rectangle.
        frugal += amount;
        area -= amount * (std::numbers::pi*pow((diameter/2),2));
        side = sqrt(area);
    }
    // Output the correct number.
    cout << (int) (frugal - wasteful) << endl;
}
