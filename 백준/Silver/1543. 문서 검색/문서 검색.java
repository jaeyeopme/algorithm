import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        String b = sc.nextLine();
        int c = 0;
        int d = a.length() - b.length() + 1;
        int ans = 0;

        for (int i = 0; i < d; i++) {
            if (c != 0) {
                c--;
                continue;
            }

            if (b.equals(a.substring(i, i + b.length())))  {
                ans++;
                c = b.length() - 1;
            }
        }

        System.out.print(ans);
    }
}