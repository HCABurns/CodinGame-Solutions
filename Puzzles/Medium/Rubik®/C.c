#include <stdio.h>
int main()
{
    int n;
    scanf("%d", &n);

    if (n == 1){
        printf("1\n");
    }else{
        printf("%d\n",(6*(n-2)*(n-2) + 12 * (n-2) + 8));
    }
    return 0;
}
