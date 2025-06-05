#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    int n;
    scanf("%d", &n);

    // Form Grid.
    int grid[n];
    for (int i = 0; i < n; i++) {
        int x;
        scanf("%d", &x);
        grid[i] = x;
    }

    // Swaps left most 0 with right most 1 until R < L.
    int swaps = 0;
    int l = 0;
    int r = n-1;
    while (l < r){
        while (l < r && grid[l] != 0){
            l += 1;
        }
        while (l < r && grid[r] != 1){
            r -= 1;
        }
        
        if (l < r){
            swaps += 1;
            l += 1;
            r -= 1;
        }
    }

    printf("%d\n",swaps);
    return 0;
}
