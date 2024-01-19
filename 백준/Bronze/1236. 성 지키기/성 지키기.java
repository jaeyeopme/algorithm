import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int N = scan.nextInt();
        int M = scan.nextInt();

        char[][] square = new char[N][M];

        for (int i = 0; i < N; i++) {
            String line = scan.next();
            for (int j = 0; j < M; j++) {
                square[i][j] = line.charAt(j);
            }
        }

        boolean[] width = new boolean[M];
        boolean[] height = new boolean[N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (square[i][j] == 'X') {
                    height[i] = true;
                    width[j] = true;
                }
            }
        }

        int wCount = 0;
        for (int i = 0; i < M; i++) {
            if (!width[i]) {
                wCount++;
            }
        }

        int hCount = 0;
        for (int i = 0; i < N; i++) {
            if (!height[i]) {
                hCount++;
            }
        }

        System.out.print(Math.max(wCount, hCount));
    }
}