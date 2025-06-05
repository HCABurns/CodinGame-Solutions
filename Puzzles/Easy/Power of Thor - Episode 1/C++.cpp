#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int light_x; // the X position of the light of power
    int light_y; // the Y position of the light of power
    int x; // Thor's starting X position
    int y; // Thor's starting Y position
    cin >> light_x >> light_y >> x >> y; cin.ignore();

    // Loop and if thor needs to move a direction, append it to output.
    while (1) {
        int remaining_turns; // The remaining amount of turns Thor can move. Do not remove this line.
        cin >> remaining_turns; cin.ignore();
        
        string leftRight = "";
        string upDown = "";

        if (light_x < x){
            leftRight="W";
            x-=1;
        }
        // If thor is left of the light, move east.
        else if (light_x > x){
            leftRight="E";
            x+=1;
        }
        // If thor is below light, move north.
        if (light_y < y){
            upDown = "N";
            y-=1;
        }
        // If thor is above light, move south.
        else if (light_y > y){
            upDown = "S";
            y+=1;
        }

        // A single line providing the move to be made: N NE E SE S SW W or NW
        cout << upDown << leftRight << endl;
    }
}
