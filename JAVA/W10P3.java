import java.io.BufferedReader;
import java.sql.Time;
import java.util.Random;

import org.w3c.dom.ranges.Range;

import javafx.animation.KeyFrame;
import javafx.animation.Timeline;
import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Arc;
import javafx.scene.shape.ArcType;
import javafx.scene.shape.Circle;
import javafx.stage.Stage;
import javafx.util.Duration;

public class W10P3 extends Application{
    public static void main(String[] args) {
        launch(args);
    }
    @Override
	public void start(Stage primaryStage){
        HBox hbox=new HBox(3);
        Button pause=new Button("Pause");
        Button resume=new Button("Resume");
        Button reverse=new Button("Reverse");
        hbox.setAlignment(Pos.CENTER);
        hbox.getChildren().addAll(pause,resume,reverse);
        BorderPane pane=new BorderPane();
        fanpane1 fan=new fanpane1();
        pane.setTop(fan);
        pane.setBottom(hbox);

        Scene scene=new Scene(pane);
        primaryStage.setTitle("旋转风车");
        primaryStage.setScene(scene);
        primaryStage.show();

        Timeline animation=new Timeline(
            new KeyFrame(Duration.millis(50),e -> fan.move())
        );
        animation.setCycleCount(Timeline.INDEFINITE);
        animation.play();

        pause.setOnAction((e ->animation.pause()));
        resume.setOnAction(e->animation.play());
        reverse.setOnAction(e->fan.reverse());
    }
}
class fanpane1 extends Pane{
    private double width=200;
    private double height=200;
    private double radius=Math.min(width,height)*0.5;
    private Circle circle= new Circle(width/2,height/2,radius);
    
    
	public fanpane1(){
        circle.setFill(Color.WHITE);
        circle.setStroke(Color.BLACK);
        getChildren().add(circle);

        //四个扇形
        for(int i =0;i<4;i++){
            Arc arc=new Arc(width/2,height/2,radius*0.85,radius*0.85,30+i*90,40);
            arc.setType(ArcType.ROUND);
            arc.setStroke(Color.BLACK);
            arc.setFill(Color.BLACK);
            getChildren().add(arc);
        }

    }
    double angle=3;
    public void move(){
        spin(angle);
    }

    public void spin(double angle){

        for(int i=1;i<5;i++){
            Arc arc=(Arc) getChildren().get(i);
            
            arc.setStartAngle(arc.getStartAngle()+angle);
        }
    }
    public void reverse(){
        angle=-angle;
    }
    public void setWidth(double a){
        this.width=a;
    }
    public void setHeight(double a){
        this.height=a;
    }
}