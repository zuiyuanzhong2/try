

import javafx.application.Application;
import javafx.geometry.HPos;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

public class W10P1 extends Application{
    private TextField tfNumber1=new TextField();
    private TextField tfNumber2=new TextField();
    private TextField tfResult=new TextField();
    private Button btMultiply=new Button("Multiply");
    private Button btAdd=new Button("Add");
    private Button btSub=new Button("Sbutract");
    private Button btDevide=new Button("Divide");
    
    @Override
    public void start(Stage primaryStage){
        GridPane gridpane=new GridPane();
        gridpane.setHgap(5);
        gridpane.setVgap(5);
        gridpane.add(new Label("Number1:"),0,0);
        gridpane.add(tfNumber1,1,0);
        gridpane.add(new Label("Number2:"),2,0);
        gridpane.add(tfNumber2,3,0);
        gridpane.add(new Label("Result:"),4,0);
        gridpane.add(tfResult,5,0);
        gridpane.add(btAdd,1,1);
        gridpane.add(btSub,2,1);
        gridpane.add(btMultiply,3,1);
        gridpane.add(btDevide, 4, 1);

        gridpane.setAlignment(Pos.CENTER);
        tfNumber1.setAlignment(Pos.CENTER);
        tfNumber2.setAlignment(Pos.CENTER);
        tfResult.setAlignment(Pos.CENTER);
        tfResult.setEditable(false);
        GridPane.setHalignment(btAdd,HPos.CENTER);
        GridPane.setHalignment(btSub, HPos.CENTER);
        GridPane.setHalignment(btMultiply, HPos.CENTER);
        GridPane.setHalignment(btDevide, HPos.CENTER);

        Scene scene=new Scene(gridpane);
        primaryStage.setTitle("简易计算器");
        primaryStage.setScene(scene);
        primaryStage.show();

        btAdd.setOnAction(e -> {
            double Number1=Double.parseDouble(tfNumber1.getText());
            double Number2=Double.parseDouble(tfNumber2.getText());
            tfResult.setText(String.valueOf(Number1+Number2));
        });
        btSub.setOnAction(e -> {
            double Number1=Double.parseDouble(tfNumber1.getText());
            double Number2=Double.parseDouble(tfNumber2.getText());
            tfResult.setText(String.valueOf(Number1-Number2));
        });
        btMultiply.setOnAction(e -> {
            double Number1=Double.parseDouble(tfNumber1.getText());
            double Number2=Double.parseDouble(tfNumber2.getText());
            tfResult.setText(String.valueOf(Number1*Number2));
        });
        btDevide.setOnAction(e -> {
            double Number1=Double.parseDouble(tfNumber1.getText());
            double Number2=Double.parseDouble(tfNumber2.getText());
            tfResult.setText(String.valueOf(Number1/Number2));
        });
    }
    public static void main(String[] args) {
        launch(args);
    }
}