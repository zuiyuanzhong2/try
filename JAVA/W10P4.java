
import javafx.event.ActionEvent;
import javafx.util.Duration;
import javafx.event.EventHandler;
import java.util.Calendar;
import java.util.GregorianCalendar;

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
import javafx.scene.shape.Circle;
import javafx.scene.shape.Line;
import javafx.scene.text.Text;
import javafx.stage.Stage;

public class W10P4 extends Application{
	@Override
    public void start(Stage primaryStage){
        clockpane clock=new clockpane();
        HBox hbox=new HBox(3);
        Button stop=new Button("Stop");
        Button start=new Button("Start");
        hbox.getChildren().addAll(stop,start);
        hbox.setAlignment(Pos.CENTER);

        BorderPane pane=new BorderPane();
        pane.setCenter(clock);
        pane.setBottom(hbox);

        Scene scene=new Scene(pane,500,500);
        primaryStage.setTitle("表");
        primaryStage.setScene(scene);
        primaryStage.show();

        stop.setOnAction(e-> clock.stop());
        start.setOnAction(e-> clock.start());
        
        

    }
    public static void main(String[] args) {
		launch(args);
	}

}

class clockpane extends Pane{
	private int hour;
	private int minute;
	private int second;
	
	private double w=500,h=500;
	EventHandler<ActionEvent> eventHandler=e -> {
        setCurrentTime();
    };
    Timeline animation=new Timeline(
    		new KeyFrame(Duration.millis(1000),eventHandler));

    
	
	public clockpane() {
		setCurrentTime();
        animation.setCycleCount(Timeline.INDEFINITE);
        animation.play();
	}
	public clockpane(int hour,int minute, int second) {
		this.hour=hour;
        this.minute=minute;
        this.second=second;
        paintClock();
        animation.setCycleCount(Timeline.INDEFINITE);
        animation.play();
	}
    public void pause(){
        animation.pause();
    }
    public void start(){
        animation.play();
    }
    public void stop(){
        animation.stop();
    }
    public int gethour(){
        return hour;
    }
    public int getminute(){
        return minute;
    }
    public int getsecond(){
        return second;
    }
    public void sethour(int hour){
        this.hour=hour;
        paintClock();
    }
    public void setminute(int minute){
        this.minute=minute;
        paintClock();
    }
    public void setsecond(int second){
        this.second=second;
        paintClock();
    }    

    public double getW(){
        return w;
    }
    public void setW(double w){
        this.w=w;
        paintClock();
    }
    public double getH(){
        return h;
    }
    public void setH(double h){
        this.h=h;
        paintClock();
    }
    
    public void setCurrentTime(){
        Calendar calender =new GregorianCalendar();
        this.hour=calender.get(Calendar.HOUR_OF_DAY);
        this.minute=calender.get(Calendar.MINUTE);
        this.second=calender.get(Calendar.SECOND);
        paintClock();
    }
    private void paintClock(){
        double clockRadius=Math.min(w, h)*0.8*0.5;
        double centerX=w/2;
        double centerY=h/2;
        
        Circle circle = new Circle(centerX,centerY,clockRadius);
        circle.setFill(Color.WHITE);
        circle.setStroke(Color.BLACK);
        getChildren().add(circle);
        //画出十二个数字及其对应的刻度
        double nlength=clockRadius*0.83;
        double vlength=clockRadius*0.9;
        for(int i=0;i<12;i++){
            double numx=centerX+nlength*Math.cos(i*Math.PI/6);
            double numy=centerY+nlength*Math.sin(i*Math.PI/6);
            double vx=centerX+vlength*Math.cos(i*Math.PI/6);
            double vy=centerY+vlength*Math.sin(i*Math.PI/6);
            double vendx=centerX+clockRadius*Math.cos(i*Math.PI/6);
            double vendy=centerY+clockRadius*Math.sin(i*Math.PI/6);
            int num=(15+i)%12;
            Text t=new Text(numx-5,numy+5,String.valueOf(num));
            Line line=new Line(vx,vy,vendx,vendy);
            getChildren().add(t);
            getChildren().add(line);
        }
        //画出完整的六十个刻度
        double alength=clockRadius*0.95;
        for(int i=0;i<60;i++) {
        	double ax=centerX+alength*Math.cos(i*Math.PI/30);
            double ay=centerY+alength*Math.sin(i*Math.PI/30);
            double aendx=centerX+clockRadius*Math.cos(i*Math.PI/30);
            double aendy=centerY+clockRadius*Math.sin(i*Math.PI/30);
            Line aline=new Line(ax,ay,aendx,aendy);
            getChildren().add(aline);
        }
        

        double slength=clockRadius*0.8;
        double secondX=centerX+slength*Math.sin(second*(2*Math.PI/60));
        double secondY=centerY-slength*Math.cos(second*(2*Math.PI/60));
        Line sline=new Line(centerX,centerY,secondX,secondY);
        sline.setStroke(Color.RED);
        getChildren().add(sline);

        double mlength=clockRadius*0.65;
        double minuteX=centerX+mlength*Math.sin(minute*(2*Math.PI/60));
        double minuteY=centerY-mlength*Math.cos(minute*(2*Math.PI/60));
        Line mline=new Line(centerX,centerY,minuteX,minuteY);
        mline.setStroke(Color.BLUE);
        mline.setStrokeWidth(3);
        getChildren().add(mline);

        double hlength=clockRadius*0.5;
        double hourX=centerX+hlength*Math.sin((hour%12+minute/60.0)*(2*Math.PI/12));
        double hourY=centerY-hlength*Math.cos((hour%12+minute/60.0)*(2*Math.PI/12));
        Line hline=new Line(centerX,centerY,hourX,hourY);
        hline.setStroke(Color.GREEN);
        hline.setStrokeWidth(5);
        getChildren().add(hline);

        

    }

}
