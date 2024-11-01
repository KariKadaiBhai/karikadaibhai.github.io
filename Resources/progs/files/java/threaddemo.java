import java.io.*;

class A extends Thread
{
  public void run()
  {
    for(int i=1;i<=5;i++)
    {
      System.out.println("value from a i="+i);
    }
    System.out.println("exit from A");
  }
}

class B extends Thread
{
  public void run()
  {
    for(int i=1;i<=5;i++)
    {
      System.out.println("value from b i="+i);
    }
    System.out.println("exit from B");
  }
}

class C extends Thread
{
  public void run()
  {
    for(int i=1;i<=5;i++)
    {
      System.out.println("value from c i="+i);
    }
    System.out.println("exit from C");
  }
}

class threaddemo
{
  public static void main(String args[])
  {
    new A().start();
    new B().start();
    new C().start();
  }
}