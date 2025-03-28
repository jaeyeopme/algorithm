import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String str = scan.nextLine();
        String find = scan.nextLine();
        int ans = 0;

        while (true) {
            int findIndex = str.indexOf(find);
            if (findIndex < 0) break;
            
            int startIndex = findIndex + find.length();
            str = str.substring(startIndex);
            ans++;
        }

        System.out.print(ans);
    }
    
}