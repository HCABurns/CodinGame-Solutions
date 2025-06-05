#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    #define M_PI acos(-1.0)
    float side;
    float diameter;
    scanf("%f%f", &side, &diameter);

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
         area -= amount * (M_PI*pow((diameter/2),2));
         side = sqrt(area);
     }

    // Output the correct number.
    printf("%d\n", ((int) (frugal - wasteful)));
    return 0;
}
