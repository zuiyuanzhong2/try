import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.Slider;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.scene.media.Media;
import javafx.scene.media.MediaPlayer;
import javafx.scene.media.MediaView;
import javafx.stage.Stage;

public class W11P3 extends Application {
    private static String media="C:\\book\\sample.mp4";
    @Override
    public void start(Stage primarStage){
        Media medi=new Media(media);
        MediaPlayer mediapalyer =new MediaPlayer(medi);
        MediaView mediaview=new MediaView(mediapalyer);
        Button play=new Button(">");
        play.setOnAction(e->{
            if(play.getText().equals(">")){
                mediapalyer.play();
                play.setText("||");
            }
            else{
                mediapalyer.pause();
                play.setText(">");
            }
        });
        Slider time =new Slider();
        Slider volumSlider=new Slider();
        volumSlider.setMaxWidth(150);
        volumSlider.setValue(30);
        mediapalyer.volumeProperty().bind(volumSlider.valueProperty());
        Label timenow =new Label();
        HBox hbox=new HBox(10);
        hbox.setAlignment(Pos.CENTER);
        hbox.getChildren().addAll(play,new Label("Time"),time,timenow,new Label("Volume",volumSlider));
        BorderPane pane=new BorderPane();
        pane.setCenter(mediaview);
        pane.setBottom(hbox);
        Scene scene=new Scene(pane);
        primarStage.setTitle("media");
        primarStage.setScene(scene);
        primarStage.show();
        time.valueProperty().addListener(ov->{
            if(time.isValueChanging()){
                mediapalyer.seek(mediapalyer.getTotalDuration().multiply(time.getValue()/100));
            }
        });
        mediapalyer.currentTimeProperty().addListener(ov->{
            time.setValue(mediapalyer.getCurrentTime().divide(mediapalyer.getMedia().getDuration()).toMillis()*100);
            timenow.setText(format((int)mediapalyer.getCurrentTime().toSeconds()));
        });
    }
    public static String format(long seconds){
        int hour=(int)(seconds/3600%24);
        int minute=(int)(seconds/60%60);
        int second=(int)(seconds%60);
        return (hour<10? "0" +hour:hour)+":"+(minute<10? "0" +minute:minute)+":"+(second<10? "0" +second:second);
    }
    public static void main(String[] args) {
        launch(args);
    }
}