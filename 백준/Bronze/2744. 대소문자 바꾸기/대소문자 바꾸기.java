import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        StringBuilder re = new StringBuilder();
        
        for (char c : str.toCharArray()) {
            if (Character.isUpperCase(c)) {
                re.append(Character.toLowerCase(c));
            } else {
                re.append(Character.toUpperCase(c));
            }
        }
        
        System.out.print(re);
    }    
    
}
