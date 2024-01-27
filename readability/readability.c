

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
char* get_string(void);
char* split(char *string);
int count(char*string);
void correct(char*string);
int main()
{
    printf("Enter your string :) \n");
    char *s = get_string();
    correct("we is playing football");
    return 0;
}
char* get_string(void)
{
    char *string =(char*)malloc(sizeof(char));
    int i=0;
    char c;
    while((c =getchar()) !='\n'){
    string = realloc(string,sizeof(char)*(i+1));
    *(string+i)=c;
    ++i;

    }
    *(string+i)='\0';


    return string;
}
void correct(char*string)
{
    char **string2=malloc(sizeof(char*)*strlen(string)+1);
    int i,j=0,m=0;
    while(strstr(string,"we")!=NULL)
    {
        correct(strstr(string,"we"));
    }
    for(i=0;i<strlen(string);i++)
    {
        if(string[i]==' '||string[i]=='\0')
        {
            string2[m][j]='\0';
            m++;
            j=0;

        }
        else
        {
            string2[m][j] = string[i];
            j++;
        }

    }
    for(int k=0;k < m;k++)
        printf("%s\n",string2[i]);
    if(strcmp(string2[1],"are")!=0)
    {
     string2[1]="are";
    }

}



int count(char*string)
{
    int i=0,counter=0;
    for(i;i<strlen(string);i++)
    {
        if(string[i]==' ')
        {
            counter++;
        }
    }
    return counter;
}

