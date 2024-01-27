#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#define BLOCK_SIZE 512

typedef uint8_t BYTE;
int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    FILE *f = fopen(argv[1], "r");


    if (f == NULL)
    {
        printf("couldn't open the FILE\n");
        return 1;
    }
    BYTE buffer[BLOCK_SIZE];
    char filename[8];
    int count = 0;
    FILE *img = NULL;
    while (fread(buffer, sizeof(BYTE), BLOCK_SIZE, f) == BLOCK_SIZE)
    {
        if (buffer[0] == 0xff && buffer[2] == 0xff
            && buffer[1] == 0xd8 && ((buffer[3] & 0xf0) == 0xe0))
        {
            if (count == 0)
            {
                sprintf(filename, "%03i.jpg", count);
                img = fopen(filename, "w");
                fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, img);
                count++;
            }
            else if (count > 0)
            {
                fclose(img);
                sprintf(filename, "%03i.jpg", count);
                img = fopen(filename, "w");
                fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, img);
                count++;

            }
        }
        else if (count > 0)
        {
            fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, img);
        }
    }
    fclose(img);
    fclose(f);
    return 0;
}
