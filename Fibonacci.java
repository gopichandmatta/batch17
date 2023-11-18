import java.util.Scanner;
class Fibonacci
{
public static void main(String[]args)
{
Scanner scan=new Scanner(System.in);
System.out.println("enter the no.of series you want:");
int n=scan.nextInt();
int a=0;
int b=1;
int c;
for(int i=0;i<=n;i++)
{
System.out.println(a);
c=a+b;
a=b;
b=c;
}
}
}
