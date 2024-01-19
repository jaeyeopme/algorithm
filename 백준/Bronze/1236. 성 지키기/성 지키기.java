import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int N = scan.nextInt();
        int M = scan.nextInt();

        boolean[] row = new boolean[M];
        boolean[] column = new boolean[N];

        int rowCount = M;
        int columnCount = N;

        for (int i = 0; i < N; i++) {
            char[] line = scan.next().toCharArray();
            for (int j = 0; j < M; j++) {
                if (line[j] == 'X') {
                    if (!row[j]) {
                        row[j] = true;
                        rowCount--;
                    }
                    if (!column[i]) {
                        column[i] = true;
                        columnCount--;
                    }
                }
            }
        }

        System.out.print(Math.max(rowCount, columnCount));
    }
}