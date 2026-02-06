import java.util.*;
import java.util.stream.*;
import java.io.*;

public class Main {
    static BufferedReader br;
    static BufferedWriter bw;
    static int N, K, count = 0, tar;
    static LinkedList<Integer> list;
    static StringJoiner sj;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] strs = br.readLine().split(" ");
        N = Integer.parseInt(strs[0]);
        K = Integer.parseInt(strs[1]);

        list = IntStream.range(1, N + 1).boxed().collect(Collectors.toCollection(LinkedList::new));

        bw.write('<');

        sj = new StringJoiner(", ");

        while (!list.isEmpty()) {
            tar = list.removeFirst();

            if (++count == K) {
                sj.add(String.valueOf(tar));
                count = 0;
            } else {
                list.addLast(tar);
            }
        }

        bw.write(sj.toString());
        bw.write('>');
        bw.flush();
        bw.close();
    }
}