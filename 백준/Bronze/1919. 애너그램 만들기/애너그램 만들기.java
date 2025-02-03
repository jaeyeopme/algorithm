import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        char[] a1 = scan.nextLine().toCharArray();
        char[] a2 = scan.nextLine().toCharArray();
        int[] a3 = new int[26];
        int answer = 0;
        
        for (char c : a1) a3[c - 'a'] += 1;
        for (char c : a2) a3[c - 'a'] -= 1;
        for (int i : a3) answer += Math.abs(i);
        
        System.out.print(answer);
    }
    
}