import java.io.*;

class cmdline
{
  public static void main(String args[]) //args[0]=12 args[1]= 15.5 args[2]= SRM
  { 
    int a;
    float b,c;
    String s;
    a=Integer.parseInt(args[0]);
    b=Float.parseFloat(args[1]);
    s=args[2];
    c=a+b;
    System.out.println("INPUT THROUGH COMMAND LINE ARGUMENTS");
    System.out.println("A="+a);
    System.out.println("B="+b);
    System.out.println("Name="+s);
    System.out.println("ADDITION OF A,B=" + c);
    System.out.println("STRING FUNCTIONS");
    System.out.println("Lower Case: "+ s.toLowerCase());
    System.out.println("UPPER Case: "+ s.toUpperCase());
    System.out.println("Length of String is : "+ s.length());
    System.out.println("String Concatenation: "+ s.concat(" IST"));
  }
}