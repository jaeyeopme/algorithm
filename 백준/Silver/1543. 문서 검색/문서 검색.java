import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        String b = sc.nextLine();
        int c = 0;
        int ans = 0;

        while (true) {
            int d = a.indexOf(b, c);

            if (d == -1) break;

            c = d + b.length();
            ans++;
        }

        System.out.print(ans);
    }
}