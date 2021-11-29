import javafx.animation.KeyFrame;
import javafx.animation.Timeline;
import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Slider;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.stage.Stage;

public class W11P2 extends Application {
    public static void main(String[] args) {
        launch(args);
    }
    @Override
	public void start(Stage primaryStage){
        HBox hbox=new HBox(3);
        fanpanecontroler fan1=new fanpanecontroler();
        fanpanecontroler fan2=new fanpanecontroler();
        fanpanecontroler fan3=new fanpanecontroler();
        hbox.getChildren().addAll(fan1,fan2,fan3);
        BorderPane pane=new BorderPane();
        pane.setTop(hbox);
        Button startall=new Button("Start All");
        Button stopall=new Button("Stop All");
        startall.setOnAction(e->{
            fan1.play();
            fan2.play();
            fan3.play();
        
        });
        stopall.setOnAction(e->{
            fan1.pause();
            fan2.pause();
            fan3.pause();
        });
        HBox hbox2=new HBox(3);
        hbox2.setAlignment(Pos.CENTER);
        hbox.getChildren().addAll(startall,stopall);
        pane.setBottom(hbox2);

        Scene scene=new Scene(pane);
        primaryStage.setTitle("变速风车");
        primaryStage.setScene(scene);
        primaryStage.show();

    }
}
class fanpanecontroler extends BorderPane{
    fanpane1 fan=new fanpane1();
    Timeline animation=new Timeline(
            new KeyFrame(Duration.millis(50),e -> fan.move())
        );
    public fanpanecontroler(){
        HBox hbox=new HBox(3);
        Button pause=new Button("Pause");
        Button resume=new Button("Resume");
        Button reverse=new Button("Reverse");
        hbox.setAlignment(Pos.CENTER);
        hbox.getChildren().addAll(pause,resume,reverse);
        Slider slider =new Slider();
        slider.setValue(10);
        this.setBottom(slider);
        this.setCenter(fan);
        this.setTop(hbox);
        animation.setCycleCount(Timeline.INDEFINITE);
        animation.play();
        pause.setOnAction((e ->animation.pause()));
        resume.setOnAction(e->animation.play());
        reverse.setOnAction(e->fan.reverse());
        slider.setMax(20);
        animation.rateProperty().bind(slider.valueProperty());
        this.widthProperty().addListener(ov-> fan.setWidth(fan.getWidth()));
        this.heightProperty().addListener(ov->fan.setHeight(fan.getHeight()));

    }
    public void play(){
        animation.play();
    }
    public void pause(){
        animation.pause();
    }
    public void reverse(){
        fan.reverse();
    }
    
    
}