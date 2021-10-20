public class W6P2 {
    public static void main(String[] args) throws CloneNotSupportedException {
        Course1 course1=new Course1("o");
        course1.addStudent("1");
        course1.addStudent("2");
        course1.addStudent("3");
        Course1 course2=(Course1)course1.clone();
        course1.addStudent("4");
        course1.addStudent("5");
        course1.addStudent("6");
        System.out.println("学生表1人数："+course1.getNumberOfStudents());
        System.out.println("学生表2人数："+course2.getNumberOfStudents());
        
    }
}
class Course1 implements Cloneable{
    private String courseName;
    private String[] students=new String[100];
    private int numberOfStudents;
    public Course1(String courseName){
        this.courseName=courseName;
    }
    public void addStudent(String student){
        students[numberOfStudents]=student;
        numberOfStudents++;
    }
    public String[] getStudents(){
        return students;
    }
    public int getNumberOfStudents(){
        return numberOfStudents;
    }
    public String getcoursename(){
        return courseName;
    }
    public void dropStudents(String student){
    }

    public Object clone() throws CloneNotSupportedException {
    return super.clone();
    }
}