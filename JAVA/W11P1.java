
import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.stage.Stage;

public class W11P1 extends Application{
    @Override 
    public void start(Stage primarStage){
        HBox hbox=new HBox(3);
        TextField htf=new TextField();
        TextField mtf=new TextField();
        TextField stf=new TextField();
        hbox.setAlignment(Pos.CENTER);
        hbox.getChildren().addAll(new Label("Hour"),htf,new Label("Minute"),mtf,new Label("Second"),stf);
        BorderPane pane=new BorderPane();
        clockpane clock=new clockpane();
        pane.setCenter(clock);
        pane.setBottom(hbox);
        Scene scene=new Scene(pane);
        primarStage.setTitle("请输入时间");
        primarStage.setScene(scene);
        primarStage.show();
        clock.widthProperty().addListener(ov ->clock.setW(pane.getWidth()));
        clock.heightProperty().addListener(ov ->clock.setH(pane.getHeight()));

        htf.setOnAction(e->{
            clock.sethour(Integer.parseInt(htf.getText()));
        });
        mtf.setOnAction(e->{
            clock.setminute(Integer.parseInt(mtf.getText()));
        });
        stf.setOnAction(e->{
            clock.setsecond(Integer.parseInt(stf.getText()));
        });

        }
    public static void main(String[] args) {
        launch(args);
        
    }
    
}