import java.io.*;

class whiledemo
{
  public static void main(String args[] )
  {
    int i=1, sum=0;
    while(i<=10)
    {
      System.out.println("i="+i);
      sum=sum+i;
      i++;
    }
    System.out.println("Sum of the series="+sum);
  }
}