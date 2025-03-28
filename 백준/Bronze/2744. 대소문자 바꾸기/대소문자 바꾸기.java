import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        char[] ca = scan.nextLine().toCharArray();

        for (int i = 0; i < ca.length; i++) {
            if (Character.isUpperCase(ca[i])) {
                ca[i] = Character.toLowerCase(ca[i]);
                continue;
            }
            ca[i] = Character.toUpperCase(ca[i]);
        }

        System.out.println(new String(ca));
    }

}
