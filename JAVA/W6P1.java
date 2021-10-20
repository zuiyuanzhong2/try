
public class W6P1{
    public static void main(String[] args) {
        Circle1 circle1 = new Circle1(5);
        Circle1 circle2 = new Circle1(4);
        Circle1 circle=(Circle1)GeometricObject1.max(circle1,circle2);
        System.out.println("更大的圆的面积是:"+circle.getArea());
        System.out.println(circle);
        Rectangle1 c1 = new Rectangle1(5,2);
        Rectangle1 c2 = new Rectangle1(4,3);
        Rectangle1 c=(Rectangle1)GeometricObject1.max(c1,c2);
        System.out.println("更大的矩形的面积是:"+c.getArea());
        System.out.println(c);

        
    }
    
    
}
abstract class GeometricObject1 implements Comparable<GeometricObject1>{
    protected String color = "white";
    protected boolean filled;
    protected java.util.Date dateCreated;

    protected GeometricObject1(){
        dateCreated=new java.util.Date();
    }
    protected GeometricObject1(String color, boolean filled){
        dateCreated=new java.util.Date();
        this.color=color;
        this.filled=filled;
    }
    @Override
    public String toString(){
        return "Created on"+dateCreated+"\ncolor:"+color+"and filled:"+filled;

    }
    public abstract double getArea();
    public int compareTo(GeometricObject1 o){
        if(getArea()<o.getArea())
            return -1;
        else if (getArea()==o.getArea())
            return 0;
        else 
            return 1;
    }
    public static GeometricObject1 max(GeometricObject1 o1,GeometricObject1 o2){
        if (o1.compareTo(o2)>0)
            return o1;
        else
            return o2;
    }
}
class Circle1 extends GeometricObject1{
    protected double radius;
    public Circle1(){
    }
    public Circle1(double radius){
        this.radius=radius;

    }
    public double getRadius(){
        return radius;
    }
    public double getArea(){
        return radius*radius*Math.PI;
    }
    @Override
    public String toString(){
        return "半径是："+radius;
    }
    
}
class Rectangle1 extends GeometricObject1{
    protected double width;
    protected double length;

    public Rectangle1(){
    }
    public Rectangle1(double width,double length){
        this.width=width;
        this.length=length;

    }
    public double getArea(){
        return width*length;
    }
    @Override
    public String toString(){
        return "长是："+length+"宽是:"+width;
    }
    
}

    
    