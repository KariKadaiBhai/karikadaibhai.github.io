import java.io.*;

class operators
{
  public static void main(String args[])
  {
    int a=100,b=200,add, sub, mul,div;
    add=a+b;
    sub=b-a;
    mul=a*b;
    div=a/b;
    System.out.println("ARITHMETIC OPERATORS:");
    System.out.println("Addition:" + add);
    System.out.println("Subtraction:"+ sub);
    System.out.println("Multiplication:"+ mul);
    System.out.println("Division:"+ div);
    System.out.println("Unary Operators: ++, --");
    System.out.println(a++);
    System.out.println(++a);
    System.out.println(a--);
    System.out.println(--a);
    System.out.println("SHIFT OPERATORS");
    System.out.println(10<<2);
    System.out.println(10<<3);
    System.out.println(20<<2);
    System.out.println(15<<4);
  }
}