#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define MIN(x, y) (((x) < (y)) ? (x) : (y))

int main()
{
    int n;
    int m;
    scanf("%d%d", &n, &m);

    // Get the number of sweets in a pile.
    int sweets[n];
    for (int i = 0; i < n; i++) {
        int x;
        scanf("%d", &x);
        sweets[i] = x;
    }

    // Bubble sort to order arr.
    int tmp = 0;
    for (int i = 0; i < n-1; i++){
        for (int j = 0; j < n-1; j++){
            if (sweets[j] > sweets[j+1]){
                tmp = sweets[j];
                sweets[j] = sweets[j+1];
                sweets[j+1] = tmp;
            }
        }
    }

    // Find the minimum difference.
    int minDifference = 999;
    for (int i = 0; i < n-m+1; i++) {
        minDifference = MIN(sweets[i+m-1] - sweets[i] , minDifference);
    }
    
    // Print the minimum difference.
    printf("%d\n",minDifference);
    return 0;
}
