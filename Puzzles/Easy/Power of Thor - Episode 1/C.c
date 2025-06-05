#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    // the X position of the light of power
    int light_x;
    // the Y position of the light of power
    int light_y;
    // Thor's starting X position
    int x;
    // Thor's starting Y position
    int y;
    scanf("%d%d%d%d", &light_x, &light_y, &x, &y);

    // game loop
    while (1) {
        // The remaining amount of turns Thor can move. Do not remove this line.
        int remaining_turns;
        scanf("%d", &remaining_turns);

        char leftRight[1] = {""};
        char upDown[1] =  {""};

        if (light_x < x){
            leftRight[0]='W';
            x-=1;
        }
        // If thor is left of the light, move east.
        else if (light_x > x){
            leftRight[0]='E';
            x+=1;
        }
        // If thor is below light, move north.
        if (light_y < y){
            upDown[0] = 'N';
            y-=1;
        }
        // If thor is above light, move south.
        else if (light_y > y){
            upDown[0] = 'S';
            y+=1;
        }

        // A single line providing the move to be made: N NE E SE S SW W or NW
        if ((upDown[0] == 'N' || upDown[0] == 'S') && (leftRight[0] == 'E' || leftRight[0] == 'W')){
            printf("%c%c\n",upDown[0],leftRight[0]);
        }
        else if (upDown[0] == 'N' || upDown[0] == 'S'){
            printf("%c\n",upDown[0]);
        }
        else{
            printf("%c\n",leftRight[0]);
        }
    }

    return 0;
}
