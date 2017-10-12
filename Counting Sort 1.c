#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

  int n;//c=0;
    scanf("%d",&n);
    int a[n],c[99]={0};
    int i=0;
    for(;i<n;i++)
        scanf("%d",&a[i]);
    for(int j=0;j<n;j++){
    for(i=0;i<=99;i++){
        if(a[j]==i)
            c[i]++;
    }}
   for(i=0;i<=99;i++)
        printf("%d ",c[i]);
    return 0;
}