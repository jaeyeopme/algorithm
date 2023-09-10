import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] a = sc.nextLine().toCharArray();
        char[] b = sc.nextLine().toCharArray();
        int[] c = new int[26];
        int answer = 0;

        for (char d : a) c[d - 'a']++;
        for (char d : b) c[d - 'a']--;
        for (int d : c) answer += Math.abs(d);

        System.out.println(answer);
    }
}