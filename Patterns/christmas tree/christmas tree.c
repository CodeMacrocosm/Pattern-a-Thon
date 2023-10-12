#include<stdio.h>
int main()
{
	int i,j;
	
	for(i=1;i<=8;i++)
	{
		printf("   \t\t");
		for(j=8;j>=1;j--)
		{
			if(j>i)
			{
				printf(" ");
			}
			else
			{
				printf("* ");
			}
			
			
		}
		printf("\n ");
	}
	for(i=1;i<=10;i++)
	{
		printf(" \t\t");
		for(j=10;j>=1;j--)
		{
			if(j>i)
			{
				printf(" ");
			}
			else
			{
				printf("* ");
			}
		}
		printf("\n");
	}
	
	for(i=1;i<=10;i++)
	{
		printf("  \t\t\t");
		for(j=1;j<=3;j++)
		{
			printf("*");
		}
		printf("\n");
	}
}