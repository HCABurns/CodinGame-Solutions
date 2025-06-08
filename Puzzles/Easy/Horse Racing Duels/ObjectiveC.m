#include <Foundation/Foundation.h>

// Comparison function for qsort
int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int main(int argc, const char * argv[]) {
    // Read in and form array.
    int N;
    scanf("%d", &N);
    int arr[N];
    for (int i = 0; i < N; i++) {
        int Pi;
        scanf("%d", &Pi);
        arr[i] = Pi;
    }

    // Sort the array.
    qsort(arr, N, sizeof(int), compare);

    // Find smallest difference.
    int diff = 999999;
    for (int i = 0; i < N-1; i++) {
        if (arr[i+1] - arr[i] < diff){
            diff = arr[i+1] - arr[i];
        }
    }

    // Print the smallest difference.
    printf("%d\n",diff); 
}
