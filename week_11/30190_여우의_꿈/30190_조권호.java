// 30190 여우의 꿈 (G5)
// https://www.acmicpc.net/problem/30190
// 정답

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static StringTokenizer stt;
	static int K, middle, ans = 0;
	static final int MOD = 1000000007;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		stt = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(stt.nextToken());
		K = Integer.parseInt(stt.nextToken());

		int[] dp = new int[N];
		if (N == 1) {
			int i = Integer.parseInt(br.readLine());
			if (K == i)
				System.out.println(0);
			else {
				System.out.println(1);
			}
		} else {
			dp[1] = 1;
			for (int i = 2; i < N; i++) {
				dp[i] = (2 * dp[i - 1] + 1) % MOD;
			}

			int[] panes = new int[N];
			stt = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				panes[i] = Integer.parseInt(stt.nextToken());
			}

			for (int i = N - 1; i > 0; i--) {
				// 1. 현재 위치면 0 2. 다른 위치면 하노이탑 n-1번째 옮기기
				if (K == panes[i])
					continue;
				ans += dp[i] + 1;
				ans %= MOD;
				K = 6 - K - panes[i];
			}

			// 마지막 값 계산
			if (K == panes[0]) {
			} else {
				ans += 1;
				ans %= MOD;
			}

			System.out.println(ans);
		}
	}
	
}
