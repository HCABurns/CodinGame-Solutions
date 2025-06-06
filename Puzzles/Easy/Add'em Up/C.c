#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

// Function to sort the array.
int cmpfunc (const void * a, const void * b)
{
   return ( *(int*)a < *(int*)b );
}

int main()
{
    // Form array of ints.
    int N;
    scanf("%d", &N);
    int cards[N];
    for (int i = 0; i < N; i++) {
        int x;
        scanf("%d", &x);
        cards[i] = x;
    }

    // Sort Arr [0..n]
    qsort(cards, N, sizeof(int), cmpfunc);

    // Set total.
    int total = 0;
    N-=1;
    while (N > 0){
        //printf("%d\n",N);
        
        int new_card = cards[N] + cards[N-1];
        total += new_card;

        // Set last item to new card.
        cards[N-1] = new_card;

        // Sort again with the new card in the list.
        qsort(cards, N, sizeof(int), cmpfunc);
        N-=1;

    }

    // Output total minimum.
    printf("%d\n",total);
    return 0;
}
