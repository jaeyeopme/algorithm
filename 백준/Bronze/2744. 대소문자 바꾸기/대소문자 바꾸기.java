import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        
        for (char c : str.toCharArray()) {
            if ('A' <= c && c <= 'Z') {
                int i = c - 'A';
                System.out.print((char) ('a' + i));
            } else {
                int i = c - 'a';
                System.out.print((char) ('A' + i));
            }
        }
    }
}