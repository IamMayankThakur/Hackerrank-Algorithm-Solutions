#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int n,i,j,key,count=0;
    scanf("%d",&n);
    int a[n];
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    for(i=1;i<n;i++){
        key=a[i];
        j=i-1;
        while(j>=0 && key<a[j])
            {
            a[j+1]=a[j];
            count++;
            j--;
        }
        a[j+1]=key;
    }
    printf("%d",count);
    return 0;
}
