import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Arc;
import javafx.scene.shape.ArcType;
import javafx.scene.shape.Circle;
import javafx.stage.Stage;

public class W9P1 extends Application{
	public static void main(String[] args) {
		launch(args);
	}

	@Override
	public void start(Stage primaryStage) {
		GridPane pane=new GridPane();
		pane.add(new fanpane(), 0, 0);
		pane.add(new fanpane(), 1, 0);
		pane.add(new fanpane(), 0, 1);
		pane.add(new fanpane(), 1,1);
		Scene scene=new Scene(pane);
		primaryStage.setTitle("MyJavaFX");
		primaryStage.setScene(scene);
		primaryStage.show();
	}

}
class fanpane extends Pane{
	double redius = 60;
	public fanpane(){
		//创建一个圆
        Circle circle= new Circle(60,60,redius);
        circle.setFill(Color.WHITE);
        circle.setStroke(Color.BLACK);
        getChildren().add(circle);
        //四个扇形
        Arc arc1=new Arc(60,60,45,45,30,40);
        arc1.setType(ArcType.ROUND);
        arc1.setStroke(Color.BLACK);
        arc1.setFill(Color.BLACK);
        getChildren().add(arc1);
        Arc arc2=new Arc(60,60,45,45,30+90,40);
        arc2.setType(ArcType.ROUND);
        arc2.setStroke(Color.BLACK);
        arc2.setFill(Color.BLACK);
        getChildren().add(arc2);
        Arc arc3=new Arc(60,60,45,45,30+180,40);
        arc3.setType(ArcType.ROUND);
        arc3.setStroke(Color.BLACK);
        arc3.setFill(Color.BLACK);
        getChildren().add(arc3);
        Arc arc4=new Arc(60,60,45,45,30+270,40);
        arc4.setType(ArcType.ROUND);
        arc4.setStroke(Color.BLACK);
        arc4.setFill(Color.BLACK);
        getChildren().add(arc4);
    }
}