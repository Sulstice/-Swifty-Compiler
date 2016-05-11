

import java.util.Arrays;
import java.util.List;

public class Stream {

    public static void streamOperation(List<Integer> number) {
        number.stream()
                .sorted()
                .map(n -> n+2)
                .forEach(n -> System.out.print(n.toString() + ", "));
    }
}