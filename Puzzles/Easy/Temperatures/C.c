#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    // Find temp closest to 0 and prioritise positive over negatives if equal.
    int n;
    scanf("%d", &n);
    int temp = -999999;
    for (int i = 0; i < n; i++) {
        int t;
        scanf("%d", &t);

        if (abs(t) < abs(temp)){
            temp = t;
        }else if (abs(t) == abs(temp)){
            if (t > temp){
                temp = t;
            }
        }
    }

    // Print correct output.
    if (temp != -999999){
        printf("%d\n",temp);
    }
    else{
        printf("0\n");
    }

    return 0;
}
