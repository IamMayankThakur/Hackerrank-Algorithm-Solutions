#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
   int v,n;
    scanf("%d%d",&v,&n);
    int a[n],i=0;
    for(;i<n;i++)
        scanf("%d",&a[i]);
    i=0;
    for(;i<n;i++)
       { if(v==a[i])
        printf("%d",i);
       }return 0;
}
