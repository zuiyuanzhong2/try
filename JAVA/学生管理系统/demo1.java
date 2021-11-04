package 学生管理系统;

import java.sql.ResultSet;
import java.sql.SQLException;

public class demo1 {
    static String sql=null;
    static DBHelper db1=null;
    static ResultSet resu=null;
    public static void main(String[] args) {
        sql="select * from Course";
        db1=new DBHelper(sql);

        try{
            resu=db1.pst.executeQuery();
            while(resu.next()){
                String CourseID = resu.getString(1);
                String  name=resu.getString(2);
                String TeacherID=resu.getString(3);
                String grade=resu.getString(4);
                System.out.println(CourseID+'\t'+name+'\t'+TeacherID+'\t'+grade);
            }
            resu.close();
            db1.close();
        }catch(SQLException e){
            e.printStackTrace();
        }
    }    
}