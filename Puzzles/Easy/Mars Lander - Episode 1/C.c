#include <stdio.h>
int main()
{
    // the number of points used to draw the surface of Mars.
    int surface_n;
    scanf("%d", &surface_n);
    for (int i = 0; i < surface_n; i++) {
        // X coordinate of a surface point. (0 to 6999)
        int land_x;
        // Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
        int land_y;
        scanf("%d%d", &land_x, &land_y);
    }

    // game loop
    while (1) {
        int X;
        int Y;
        // the horizontal speed (in m/s), can be negative.
        int h_speed;
        // the vertical speed (in m/s), can be negative.
        int v_speed;
        // the quantity of remaining fuel in liters.
        int fuel;
        // the rotation angle in degrees (-90 to 90).
        int rotate;
        // the thrust power (0 to 4).
        int power;
        scanf("%d%d%d%d%d%d%d", &X, &Y, &h_speed, &v_speed, &fuel, &rotate, &power);

        // If speed larger than landing speed, set power to max.
        if (v_speed > -39){
            power = 0;
            printf("0 0\n");
        }
        else{
            power = 4;
            printf("0 4\n");
        }
    }
    return 0;
}
