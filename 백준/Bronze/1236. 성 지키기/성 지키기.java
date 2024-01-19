import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int N = scan.nextInt();
        int M = scan.nextInt();

        boolean[] row = new boolean[M];
        boolean[] column = new boolean[N];

        int rowCount = 0;
        int columnCount = 0;

        for (int i = 0; i < N; i++) {
            char[] line = scan.next().toCharArray();
            for (int j = 0; j < M; j++) {
                if (line[j] == 'X') {
                    if (!column[i]) {
                        column[i] = true;
                        columnCount++;
                    }
                    if (!row[j]) {
                        row[j] = true;
                        rowCount++;
                    }
                }
            }
        }

        System.out.print(Math.max(M - rowCount, N - columnCount));
    }
}