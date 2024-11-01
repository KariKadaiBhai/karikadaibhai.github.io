import java.io.*;

interface I1
{
  int r=6;
}

class C1 implements I1
{
  void display()
  {
    double pi=3.14;
    System.out.println("Area of the Circle="+pi*r*r);
  }
}

class interfacedemo
{
  public static void main(String args[])
  {
    System.out.println("Interface implementation");
    C1 obj=new C1();
    obj.display();
  }
}