import java.util.*;
import java.io.*;

public class LowerCaseStream extends StreamDecorator {
  InputStream inStream;
  public LowerCaseStream(InputStream s) { inStream = s; }
  
  @Override
  public int read() throws IOException {
    return Character.toLowerCase(inStream.read());
  }

  public static void main(String[] args) {
    String str = new String ("I know the Decorator Pattern therefore I RULE!");
    InputStream stream;
    try {
      stream = new ByteArrayInputStream(str.getBytes("UTF-8"));
    }
    catch (Exception ex) {
      System.out.println (ex.toString());
      return;
    }
    InputStream lower_stream = new LowerCaseStream (stream);
    String out_str = "";
    try{
        int data = lower_stream.read();
        while (data != -1) {
          out_str = out_str + Character.toChars(data)[0];
          data = lower_stream.read();
        }
        System.out.println(out_str);
      }
    catch (Exception ex) {
      System.out.println (ex.toString());
    }
  }
}

