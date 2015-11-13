import com.google.common.math.*;
import com.google.common.base.Strings;
import com.google.common.base.Function;
import com.google.common.collect.Iterables;
import com.google.common.base.Splitter;
import java.util.*;
import java.io.*;

class GuavaTest {
  public static void main(String[] args) {
    //IntMath.checkedMultiply(Integer.MAX_VALUE, 2);
    //checkIndexElementIndex(i, A.size())
    String test = ",a,,b,";
    for (int i = 0; i < test.split(",").length; i++){
      System.out.println(test.split(",")[i]);
    }
    String[] splitted = Iterables.toArray(Iterables.transform(Splitter.on(",").split(test), new Function<String, String>(){ 
    public String apply(String s) { return Strings.emptyToNull(s); } }), String.class);
    for (int i = 0; i < splitted.length; i++) {
      System.out.println(splitted[i]);
    }
  }
}

