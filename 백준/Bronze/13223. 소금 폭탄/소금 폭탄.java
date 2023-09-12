import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] c = sc.next().split(":");
        String[] d = sc.next().split(":");

        int cs = Integer.parseInt(c[0]) * 3600 + Integer.parseInt(c[1]) * 60 + Integer.parseInt(c[2]);
        int ds = Integer.parseInt(d[0]) * 3600 + Integer.parseInt(d[1]) * 60 + Integer.parseInt(d[2]);
        int as = ds - cs;

        if (as <= 0) as += 24 * 3600;

        System.out.printf("%02d:%02d:%02d", as / 3600, (as % 3600) / 60, as % 60);
    }
}