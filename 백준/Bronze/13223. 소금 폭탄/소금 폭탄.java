import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] a = sc.nextLine().split(":");
        String[] b = sc.nextLine().split(":");
        
        int s = Integer.parseInt(b[2]) - Integer.parseInt(a[2]);
        int m = Integer.parseInt(b[1]) - Integer.parseInt(a[1]);
        int h = Integer.parseInt(b[0]) - Integer.parseInt(a[0]);
        
        if (s < 0) {
            m--;
            s += 60;
        }
        if (m < 0) {
            h--;
            m += 60;
        }
        if (h < 0 || h + m + s == 0) h += 24;
        
        System.out.printf("%02d:%02d:%02d", h, m, s);
    }
}