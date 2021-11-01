

import java.util.InputMismatchException;
import java.util.Scanner;

public class W8P1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        boolean done = false;
        while(done){
            try{
                System.out.println("请输入两个整数：");
                int a=input.nextInt();
                int b=input.nextInt();
                System.out.println("a+b="+(a+b));
                break;
            }
            catch(InputMismatchException ex){
                System.out.println("输入错误，请重新输入");
                input.nextLine();
            }
        }
    }
}