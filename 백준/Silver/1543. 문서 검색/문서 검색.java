import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        String b = sc.nextLine();
        int c = 0;
        int ans = 0;

        for (int i = 0; i < a.length() - b.length() + 1; i++) {
            if (c != 0) {
                c--;
                continue;
            }

            String d = a.substring(i, i + b.length());

            if (b.equals(d))  {
                ans++;
                c = b.length() - 1;
            }
        }

        System.out.print(ans);
    }
}