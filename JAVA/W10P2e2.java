import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.text.Text;
import javafx.stage.Stage;

public class W10P2e2 extends Application{
    @Override
    public void start(Stage primaryStage){
        Pane pane = new Pane();
        Text text=new Text();
        pane.getChildren().add(text);
        pane.setOnMousePressed(e ->{
            text.setX(e.getX());
            text.setY(e.getY());
            text.setText("("+e.getX()+","+e.getY()+")");
        });
        pane.setOnMouseReleased(e ->{
            text.setText("  ");
        });
        Scene scene=new Scene(pane,500,500);
        primaryStage.setTitle("按住鼠标显示鼠标位置，释放鼠标停止显示");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
    public static void main(String[] args) {
        launch(args);
    }
}