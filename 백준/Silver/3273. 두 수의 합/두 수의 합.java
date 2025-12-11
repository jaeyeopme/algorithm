import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int len = sc.nextInt();
		int[] arr = new int[len];
		int count = 0;

		for (int i = 0; i < len; i++) {
			arr[i] = sc.nextInt();
		}
		
		int tar = sc.nextInt();
		
		Arrays.sort(arr);
		
		int lt = 0, rt = len - 1;
		
		while (lt < rt) {
			int sum = arr[lt] + arr[rt];
			
			if (sum == tar) {
				count++;
				lt++;
				rt--;
			} else if (sum < tar) {
				lt++;
			} else {
				rt--;
			}
		}
		
		System.out.print(count);
	}
}