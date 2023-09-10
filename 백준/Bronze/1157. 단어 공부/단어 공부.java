import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] a = sc.next().toUpperCase().toCharArray();

        if (a.length == 1) {
            System.out.print(a[0]);
            return;
        }

        // A - Z
        int[] b = new int[26];
        for (char c : a) b[c - 'A']++;

        int d = 0;
        char ans = ' ';

        for (int i = 0; i < b.length; i++) {
            if (b[i] > d) {
                d = b[i];
                ans = (char) ('A' + i);
            } else if (b[i] == d) {
                d = b[i];
                ans = '?';
            }
        }

        System.out.print(ans);
    }
}