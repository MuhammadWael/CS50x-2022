#include "helpers.h"
#include<math.h>
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int avr;
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            avr = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);
            image[i][j].rgbtRed = avr;
            image[i][j].rgbtGreen = avr;
            image[i][j].rgbtBlue = avr;
        }
    }
    return;
}
int colour_limit(int rgb)
{
    if (rgb > 255)
    {
        rgb = 255;
    }
    return rgb;
}
// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    float sepiaRed, sepiaGreen, sepiaBlue;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            sepiaRed = .393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue;
            sepiaGreen = .349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue;
            sepiaBlue = .272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue;
            image[i][j].rgbtRed = colour_limit(round(sepiaRed));
            image[i][j].rgbtGreen = colour_limit(round(sepiaGreen));
            image[i][j].rgbtBlue = colour_limit(round(sepiaBlue));
        }
    }
    return;
}

// Reflect image horizontally
void swap(RGBTRIPLE *r, RGBTRIPLE *l)
{
    RGBTRIPLE temp = *r;
    *r = *l;
    *l = temp;
}
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            swap(&image[i][j], &image[i][width - j - 1]);
        }
    }

    return;
}

// Blur image

void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    for (int i = 0 ; i < height ; i++)
    {
        for (int j = 0 ; j < width ; j++)
        {
            float totalRed = 0, totalBlue = 0, totalGreen = 0, count = 0;
            for (int k = i - 1 ; k < (i + 2); k++)
            {
                for (int l = j - 1; l < (j + 2); l++)
                {
                    if (k < 0 || k > (height - 1) || l < 0 || l > (width - 1))
                    {
                        continue;
                    }
                    totalRed += image[k][l].rgbtRed;
                    totalGreen += image[k][l].rgbtGreen;
                    totalBlue += image[k][l].rgbtBlue;
                    count++;
                }
                temp[i][j].rgbtRed = round(totalRed / count);
                temp[i][j].rgbtGreen = round(totalGreen / count);
                temp[i][j].rgbtBlue = round(totalBlue / count);
            }
        }
    }



    for (int i = 0 ; i < height ; i++)
    {
        for (int j = 0 ; j < width ; j++)

        {
            image [i][j].rgbtRed = temp[i][j].rgbtRed;
            image [i][j].rgbtBlue = temp[i][j].rgbtBlue;
            image [i][j].rgbtGreen = temp[i][j].rgbtGreen;
        }
    }
    return;
}
