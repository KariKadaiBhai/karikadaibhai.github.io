import java.io.*;
import java.util.Scanner;

class switchdemo
{
  public static void main(String args[])
  {
    int day;
    Scanner console = new Scanner(System.in);
    System.out.println("Days of a week");
    System.out.println("Enter your choice");
    day = console.nextInt();
    
    switch(day)
    {
      case 1:
        System.out.println("Sunday");
        break;
      case 2:
        System.out.println("Monday");
        break;
      case 3:
        System.out.println("Tuesday");
        break;
      case 4:
        System.out.println("Wednesday");
        break;
      case 5:
        System.out.println("Thursday");
        break;
      case 6:
        System.out.println("Friday");
        break;
      case 7:
        System.out.println("Saturday");
        break;
    }
  }
}