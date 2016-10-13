#include<stdio.h>
int main()
{
    int i,j,n;
    char a[50],c[26];
    char b[26]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};

    for(i=0;i<5;i++)
        scanf("%c",&a[i]);
    for(i=0;i<50;i++)
        for( j=0;j<26;j++)
    {

        if(strcmpi(a[i],b[j])==0)
        {
            c[j]+=1;

        }

    }
    for(i=0;i<50;i++)
    {
       printf(b[i],"=",c[i]);

    }
return 0;

}
