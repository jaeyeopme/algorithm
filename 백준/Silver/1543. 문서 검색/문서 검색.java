import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String str = scan.nextLine();
        String find = scan.nextLine();
        int ans = 0;
        
        while (str.contains(find)) {
            str = str.substring(str.indexOf(find) + find.length());
            ans++;
        }
        
        System.out.print(ans);
    }
    
}