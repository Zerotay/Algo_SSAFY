// 11058 크리보드(G5)
// https://www.acmicpc.net/problem/11058
// 정답

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static int N;
	static long[] dp;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		dp= new long[101];
		
		for (int i = 1; i <= 6; i++) {
			dp[i] = i;
		}

		for (int i = 7; i <= N; i++) {
			for (int j = 3; j <= i; j++) {
				dp[i] = Math.max(dp[i], dp[i-j]*(j-1));
			}
		}
		System.out.println(dp[N]);
	}
}

// N*N이면 충분 & dp로 풀때는 long으로 배열 만들자
// 붙여넣기 하려면 3개를 잡아먹으므로 최소 3번째 전 값에 붙여넣기 값을 곱한 것과 비교