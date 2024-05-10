#include <stdio.h>
int main()
{
    int n,c=1;
    scanf("%d", &n);
    if(n==1) {printf("1/1");return 0;}
    while(n-c>0) {n-=c;c++;}
    c++;
    if((c-1)%2) printf("%d/%d",c-n,n);
    else printf("%d/%d",n,c-n);
}