import java.util.Scanner;  
public class ChristmasTreePattern1  
{  
public static void main(String args[])   
{  
Scanner sc = new Scanner(System.in);  
System.out.print("Enter the height of tree: ");  
int h = sc.nextInt();  
//beginning of upper part  
for(int i = 1;i <= h;i++)  
{  
for(int j = h-i;j > 0;j--)  
{  
System.out.print(" ");  
}  
for(int k = 1;k <= i;k++)  
{  
System.out.print("* ");  
}  
System.out.println();  
}  
//end of upper part  
//beginning of lower part  
for(int i = 1;i <= h-1;i++)  
{  
System.out.print(" ");  
for(int j = h-3;j > 0;j--)  
{  
System.out.print(" ");  
}  
for(int k = 2;k > 0;k--)  
{  
System.out.print("| ");  
}  
System.out.println();  
}// end of lower part  
}  
}  

