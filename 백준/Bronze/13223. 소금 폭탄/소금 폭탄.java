import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String[] time1 = scan.nextLine().split(":");
        String[] time2 = scan.nextLine().split(":");

        int h = Integer.parseInt(time2[0]) - Integer.parseInt(time1[0]);
        int m = Integer.parseInt(time2[1]) - Integer.parseInt(time1[1]);
        int s = Integer.parseInt(time2[2]) - Integer.parseInt(time1[2]);

        if (s < 0) {
            m--;
            s += 60;
        }
        if (m < 0) {
            h--;
            m += 60;
        }
        if (h < 0 || h + m + s == 0) {
            h += 24;
        }

        System.out.printf("%02d:%02d:%02d", h, m, s);
    }
    
}