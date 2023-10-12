// 1106 Cubeditor (G3)
// https://www.acmicpc.net/problem/1701
// 정답

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String text = br.readLine();

		int tlen = text.length();
		int max = 0;
		
		for (int l = 0; l < tlen; l++) {
			String str = text.substring(l);
			int plen = str.length();
			int[] p = new int[plen];
			
			for (int i = 1, j = 0; i < plen; i++) {
				while (j > 0 && str.charAt(i) != str.charAt(j))
					j = p[j - 1];
				if (str.charAt(i) == str.charAt(j)) {
					p[i] = ++j;
					max = Math.max(j, max);
				}
			}
		}
		System.out.println(max);
	}
}

// KMP 쓰면 끝