#include <stdio.h>

int main()
{
    // game loop
    while (1) {
        // Define required variables.
        int max_val = 0;
        int max_index = 0;

        // Find the index of the max height and store in max_index.
        for (int i = 0; i < 8; i++) {
            int mountain_h;
            scanf("%d", &mountain_h);
            if (mountain_h > max_val){
                max_val = mountain_h;
                max_index = i;
            } 
        }
        // Output the index of the mountain to fire on.
        printf("%d\n",max_index); 
    }
    return 0;
}
