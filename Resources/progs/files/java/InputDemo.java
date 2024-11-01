//Input through keyboard ://InputStream Reader
import java.io.*;
class InputDemo
{
  public static void main(String args[])
  {
    int a;
    float b,c;
    String s;
    try
    {
      DataInputStream dis=new DataInputStream(System.in);
      System.out.println("Enter a Numberic Value");
      a=Integer.parseInt(dis.readLine());
      System.out.println("Enter a Floating point Value");
      b=Float.parseFloat(dis.readLine());
      System.out.println("Enter a String Value");
      s=dis.readLine();
      System.out.println("A="+a);
      System.out.println("B="+b);
      System.out.println("S="+s);
      System.out.println("C=A+B:"+(a+b));
    }
    catch(Exception e)
    {
      System.out.println(e);
    }
  }
}