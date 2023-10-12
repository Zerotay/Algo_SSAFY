// 11568 민균이의 계략 (S2)
// https://www.acmicpc.net/problem/11568
// 정답

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int N = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());

		int[] cards = new int[N];
		for (int i = 0; i < N; i++) {
			cards[i] = Integer.parseInt(st.nextToken());
		}
		
		int[] lis = new int[N];
		int max = 0;
		for (int i = 0; i < N; i++) {
			lis[i] = 1; 
			for (int j = 0; j < i; j++) {
				if (cards[j] < cards[i] && lis[i] < lis[j] + 1) {
					lis[i] = lis[j] + 1;
				}
			}
			if (max < lis[i])
				max = lis[i];
		}
		System.out.println(max);
	}
}

// 그냥 LIS