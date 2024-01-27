#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[])
{
    if((argc == 2) && isdigit(argv[1]))
    {
       int k = atoi(argv[1]);
        p = get_string("plaintext: ");
       printf("Ciphertext: ");
       for(int i=0;i<strlen(p);i++)
       {
           if(isupper(p[i]))
           {
               char c = ((p[i]-'A')+k)%26+'A';
               printf(%c,c);
           }
           else if(islower(p[i]))
           {
               char c = (((p[i]-'a')+k)%26+'a');
               printf(%c,c);
           }
           else printf(%c,p[i]);
       }

    return 1;
    }
     else printf("Usage: ./caesar key\n");
     return 1;

}
