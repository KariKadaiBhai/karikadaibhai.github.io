import java.io.*;

class exceptiondemo
{
  public static void main(String args[])
  {
    int a=10,b=5,c=5;
    int x=a/(b-c);
    System.out.println("X="+ x);
    int y=a/(b+c);
    System.out.println("Y="+ y);
  }
}