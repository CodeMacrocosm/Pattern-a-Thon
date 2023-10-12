#include<stdio.h>
int main() {
   int a, b, line = 12;
   for (a = line/2; a <= line; a = a+2) { //for the upper part of the heart
      for (b = 1; b < line-a; b = b+2) //create space before the first peak
         printf(" ");
      for (b = 1; b <= a; b++) //print the first peak
         printf("*");
      for (b = 1; b <= line-a; b++) //create space before the first peak
         printf(" ");
      for (b = 1; b <= a-1; b++) //print the second peak
         printf("*");
      printf("\n");
   }
   for (a = line; a >= 0; a--) { //the base of the heart is inverted triangle
      for (b = a; b < line; b++) //generate space before triangle
         printf(" ");
      for (b = 1; b <= ((a * 2) - 1); b++) //print the triangle
         printf("*");
      printf("\n");
   }
}
