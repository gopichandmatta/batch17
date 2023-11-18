import java.util.Scanner;
class Palindrome1
{
public static void main(String[]args)
{
Scanner scan=new Scanner(System.in);
System.out.println("enter the number");
int number=scan.nextInt();
int temp=number;
int rev=0;
while(number>0)
{
int rem=number%10;
rev=rev*10+rem;
number=number/10;
}
if(temp==rev)
{
System.out.println(temp+"is palindrome");
}
else
{
System.out.println(temp+"is not a palindrome");
}
}
}

