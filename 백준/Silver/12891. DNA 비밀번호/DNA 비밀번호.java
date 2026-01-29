import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		char[] DNA = {'A', 'C', 'G', 'T'};
		int[] COUNT = new int[4];
		int S = Integer.parseInt(st.nextToken());
		int P = Integer.parseInt(st.nextToken());
		int ANSWER = 0;
		
		Map<Character, Integer> map = new HashMap<>();
		for (char c : DNA) map.put(c, 0);
		
		char[] text = br.readLine().toCharArray();
		
		for (int i = 0; i < P; i++) {
			if (map.containsKey(text[i])) {
				map.put(text[i], map.get(text[i]) + 1);
			}
		}
		
		st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < 4; i++) {
			COUNT[i] = Integer.parseInt(st.nextToken());
		}
		
		for (int end = P - 1; end < S; end++) {
			int start = end - P + 1;
			boolean invalid = false;
			
			for (int i = 0; i < DNA.length; i++) {
				if (COUNT[i] == 0) continue;
				
				if (map.get(DNA[i]) < COUNT[i]) {
					invalid = true;
					break;
				}
			}
			
			if (!invalid) ANSWER++;
					
			if (end == S - 1) break;
		
			map.put(text[start], map.get(text[start]) - 1);
			map.put(text[end + 1], map.get(text[end + 1]) + 1);
		}
		
		bw.write(String.valueOf(ANSWER));
		bw.flush();
		bw.close();
	}
}