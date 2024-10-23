#include <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {

    // game loop
    while (1) {
        // Declare required variables.
        int max_v = 0;
        int max_i = 0;

        // Find the index of the max height and store in max_i.
        for (int i = 0; i < 8; i++) {
            int mountainH;
            scanf("%d", &mountainH);
            if (mountainH > max_v){
                max_v = mountainH;
                max_i = i;
            }
        }
        
        // Output the index of the mountain to fire on.
        printf("%d\n",max_i); 
    }
}
