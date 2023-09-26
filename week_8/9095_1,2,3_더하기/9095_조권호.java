// 9095 1, 2, 3 더하기(S3)
// https://www.acmicpc.net/problem/9095
// 정답

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int i = 0; i < T; i++) {
			int N = Integer.parseInt(br.readLine());
			int[] dp = new int[12];
			dp[1] = 1;
			dp[2] = 2;
			dp[3] = 4;
			if (N < 4)
				System.out.println(dp[N]);
			else {
				for (int j = 4; j < N + 1; j++) {
					dp[j] = dp[j - 1] + dp[j - 2] + dp[j - 3];
				}
				System.out.println(dp[N]);
			}
		}
	}
}
# 1,2,3이 더해질 것이므로 i-1,2,3 을 다 더하면 된다.