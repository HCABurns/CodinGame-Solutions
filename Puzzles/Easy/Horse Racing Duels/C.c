#include <stdlib.h>
#include <stdio.h>

// Comparison function
int compare(const void* a, const void* b) {
   return (*(int*)a - *(int*)b);
}

int main()
{
    // Get size of array required
    int N;
    scanf("%d", &N);
    
    //Create array
    int arr[N];

    // Fill in array with horse strength
    for (int i = 0; i < N; i++) {
        int pi;
        scanf("%d", &pi);
        arr[i] = pi;
    }

    // Sort array
    qsort(arr, N, sizeof(int), compare);

    //Define difference
    int difference = 99999999;
    
    // Check adjacent horses power and store minimum difference.
    for (int i = 0; i < N-1; i++) {
        int val = arr[i+1] - arr[i];
        if (val < difference){
            difference = val;
        }
    }

    // Print output
    printf("%d\n",difference);
    return 0;
}
