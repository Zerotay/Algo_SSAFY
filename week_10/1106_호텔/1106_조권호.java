// 1106 호텔 (G5)
// https://www.acmicpc.net/problem/1106
// 정답

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static final int INF = Integer.MAX_VALUE;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int C = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());

		int[][] arr = new int[N][2];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			arr[i][0] = Integer.parseInt(st.nextToken());
			arr[i][1] = Integer.parseInt(st.nextToken());
		}

		int[] dp = new int[C + 101];    // 적어도 C명이라서 그 이상 값을 찾아도 됨
		Arrays.fill(dp, INF);
		dp[0] = 0;

		for (int i = 0; i < N; i++) {
			int cost = arr[i][0];
			int cust = arr[i][1];
			for (int j = cust; j < C + 101; j++) {
				if (dp[j - cust] != INF) {
					dp[j] = Math.min(dp[j - cust] + cost, dp[j]);
				}
			}
		}

		int ans = INF;
		for (int i = C; i < C + 101; i++) {
			ans = Math.min(ans, dp[i]);
		}

		System.out.println(ans);

	}

}