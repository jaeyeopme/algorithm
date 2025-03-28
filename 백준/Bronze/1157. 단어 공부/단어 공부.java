import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] a = sc.next().toUpperCase().toCharArray();

        if (a.length == 1) {
            System.out.println(a[0]);
            return;
        }

        // A - Z
        int[] b = new int[26];
        for (char e : a) b[e - 'A']++;

        int maxCount = 0;
        char ans = 'A';

        for (int i = 0; i < b.length; i++) {
            if (b[i] > maxCount) {
                maxCount = b[i];
                ans = (char) ('A' + i);
            } else if (b[i] == maxCount) {
                maxCount = b[i];
                ans = '?';
            }
        }

        System.out.println(ans);
    }
}