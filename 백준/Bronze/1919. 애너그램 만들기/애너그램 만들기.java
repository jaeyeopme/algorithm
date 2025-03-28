import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s1 = scan.nextLine();
        String s2 = scan.nextLine();
        int[] a3 = new int[26];
        int answer = 0;
        
        for (int i = 0; i < s1.length(); i++) a3[s1.charAt(i) - 'a'] += 1;
        for (int i = 0; i < s2.length(); i++) a3[s2.charAt(i) - 'a'] -= 1;
        for (int i : a3) answer += Math.abs(i);
        
        System.out.print(answer);
    }
    
}