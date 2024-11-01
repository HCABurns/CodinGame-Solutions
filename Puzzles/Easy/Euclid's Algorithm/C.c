#include <stdlib.h>

int main()
{
    // Get values to be used to find GCD.
    int a;
    int b;
    scanf("%d%d", &a, &b);
    int a_start = a;
    int b_start = b;

    // Continue until remainder is 0.
    while (b != 0){
        printf("%d=%d*%d+%d\n",a,b,a/b,a%b);
        int tmp = a % b;
        a = b;
        b = tmp;
    }

    // Output the GCD of a and b.
    printf("GCD(%d,%d)=%d\n",a_start,b_start,a);
    return 0;
}
