import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        String b = sc.nextLine();
        int c = a.length() - a.replace(b, "").length();
        
        System.out.print(c / b.length());
    }
}