import java.io.*;

class Room
{
  int length,width;
  Room(int x, int y)
  {
    length = x;
    width = y;
  }
  int area()
  {
    return(length*width);
  }
}

class PoojaRoom extends Room
{
  int height;
  PoojaRoom(int x,int y, int z)
  { 
    super(x,y);
    height = z;
  }
  int volume()
  {
    return(length*width*height);
  }
}

public class Inherit2
{
  public static void main(String args[])
  {
    PoojaRoom P = new PoojaRoom(10,30,40);
    int A = P.area();
    int V = P.volume();
    System.out.println("INHERITANCE");
    System.out.println("From Super-Class");
    System.out.println("Area="+A);
    System.out.println("From Sub-Class");
    System.out.println("Volume="+V);
  }
}