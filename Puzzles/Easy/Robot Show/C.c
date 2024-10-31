#include <stdio.h>

int main()
{
    // Get inputs.
    int L;
    scanf("%d", &L);
    int N;
    scanf("%d", &N);

    // Create array of bots positions.
    int arr[N];
    for (int i = 0; i < N; i++) {
        int b;
        scanf("%d", &b);
        arr[i] = b;
    }

    // Get min and max.
    int length = sizeof(arr) / sizeof(arr[0]);
    int minVal = arr[0];
    int maxVal = arr[0];
    for (int i = 0; i < length; i++) {
        if (minVal > arr[i]) {
            minVal = arr[i];
        }
        if (maxVal < arr[i]){
            maxVal = arr[i];
        }
    }

    // Max time is for a furthest box from the end to reach the end.
    if (L-minVal > maxVal){
    printf("%d\n",L-minVal);
    }else{
        printf("%d\n",maxVal);
    }
    return 0;
}
