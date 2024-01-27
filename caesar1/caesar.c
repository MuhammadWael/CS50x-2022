#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
int main(int argc, string argv[])
{
    if((argc == 2) && isdigit(*argv[1]))
    {

       int k = atoi(argv[1]);
       string p = get_string("plaintext: ");
       printf("Ciphertext: ");
       for(int i=0;i<strlen(p);i++)
       {
           if(isupper(p[i]))
           {
               printf("%c",(((p[i]-'A')+k)%26)+'A');
           }
           else if(islower(p[i]))
           {
               printf("%c",(((p[i]-'a')+k)%26)+'a');
           }
           else printf("%c",p[i]);
       }

            printf("\n");
     }
     else{
        printf("Usage: ./caesar key\n");
        return 1;
     }
     return 0;
}
