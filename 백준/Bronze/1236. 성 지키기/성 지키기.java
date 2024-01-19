import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int N = scan.nextInt();
        int M = scan.nextInt();

        boolean[] width = new boolean[M];
        boolean[] height = new boolean[N];

        for (int i = 0; i < N; i++) {
            char[] line = scan.next().toCharArray();
            for (int j = 0; j < M; j++) {
                if (line[j] == 'X') {
                    height[i] = true;
                    width[j] = true;
                }
            }
        }

        int wCount = 0;
        int hCount = 0;

        for (int i = 0; i < M; i++) {
            if (!width[i]) {
                wCount++;
            }
        }

        for (int i = 0; i < N; i++) {
            if (!height[i]) {
                hCount++;
            }
        }

        System.out.print(Math.max(wCount, hCount));
    }
}