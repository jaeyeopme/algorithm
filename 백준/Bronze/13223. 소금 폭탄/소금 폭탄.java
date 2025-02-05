import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String[] sTime1 = scan.nextLine().split(":");
        String[] sTime2 = scan.nextLine().split(":");
        int[] ans = new int[3];
        ans[0] = 24;

        if (!(sTime1[2].equals(sTime2[2]) &&
                sTime1[1].equals(sTime2[1]) &&
                sTime1[0].equals(sTime2[0]))) {
            int[] time1 = new int[3];
            int[] time2 = new int[3];

            for (int i = 0; i < 3; i++) {
                time1[i] = Integer.parseInt(sTime1[i]);
                time2[i] = Integer.parseInt(sTime2[i]);
            }

            // second
            if (time2[2] < time1[2]) {
                time2[1]--;
                ans[2] = (time2[2] + 60) - time1[2];
            } else {
                ans[2] = time2[2] - time1[2];
            }

            // minute
            if (time2[1] < time1[1]) {
                time2[0]--;
                ans[1] = (time2[1] + 60) - time1[1];
            } else {
                ans[1] = time2[1] - time1[1];
            }

            // hour
            if (time2[0] < time1[0]) {
                ans[0] = (time2[0] + 24) - time1[0];
            } else {
                ans[0] = time2[0] - time1[0];
            }
        }

        System.out.printf("%02d:%02d:%02d", ans[0], ans[1], ans[2]);
    }
    
}