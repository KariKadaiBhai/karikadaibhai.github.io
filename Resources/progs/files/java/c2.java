import p1.*;
public class c2
{
  public static void main(String args[])
  {
    c1 obj=new c1();
    obj.display();
    System.out.println("I am in the main class");
    int a=30, b=40;
    int c=a+b;
    System.out.println("A=" +a);
    System.out.println("B=" +b);
    System.out.println("Addition of A,B=" +c);
  }
}