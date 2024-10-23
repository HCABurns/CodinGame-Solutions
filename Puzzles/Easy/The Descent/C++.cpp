#include <iostream>
using namespace std;

int main()
{
    // game loop
    while (1) {
        // Define required variables.
        int max_index = 0;
        int max_value = 0;

        // Find the index of the max height and store in max_index.
        for (int i = 0; i < 8; i++) {
            int mountain_h;
            cin >> mountain_h; cin.ignore();
            if (mountain_h > max_value){
                max_value = mountain_h;
                max_index = i;
            }
        }
         // Output the index of the mountain to fire on.
        cout << max_index << endl;
    }
}
