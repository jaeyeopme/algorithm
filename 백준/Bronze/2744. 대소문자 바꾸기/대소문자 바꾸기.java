import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        for (char c : new Scanner(System.in).next().toCharArray()) {
            if ('A' <= c && c <= 'Z') {
                int i = c - 'A';
                // A - Z 사이의 순번
                System.out.print((char) ('a' + i));
            } else {
                // a - z 사이의 순번
                int i = c - 'a';
                System.out.print((char) ('A' + i));
            }
        }
    }
}