import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] a = sc.next().toUpperCase().toCharArray();

        if (a.length == 1) {
            System.out.println(a[0]);
            return;
        }

        // first, second
        int c = 0, d = 1;

        // A - Z
        int[] b = new int[26];
        for (char e : a) b[e - 'A']++;

        char ans;

        if (b[1] > b[0]) {
            c = 1;
            d = 0;
        }

        for (int i = 2; i < b.length; i++) {
            if (b[i] > b[c]) {
                c = i;
            } else if (b[i] > b[d]) {
                d = i;
            }
        }

        if (b[c] == b[d]) {
            ans = '?';
        } else if (b[c] > b[d]) {
            ans = (char) ('A' + c);
        } else {
            ans = (char) ('A' + d);
        }

        System.out.println(ans);
    }
}