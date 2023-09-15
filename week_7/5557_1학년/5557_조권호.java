// 5557 1학년(G5)
// https://www.acmicpc.net/problem/5557
// 정답

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static long[][] dp;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		dp = new long[N][21];

		StringTokenizer st = new StringTokenizer(br.readLine());
		dp[1][Integer.parseInt(st.nextToken())] = 1;

		for (int i = 2; i < N; i++) {
			int cur = Integer.parseInt(st.nextToken());
			for (int j = 0; j < 21; j++) {
				if (j - cur >= 0)
					dp[i][j] += dp[i - 1][j - cur];
				if (j + cur < 21)
					dp[i][j] += dp[i - 1][j + cur];
			}
		}
		System.out.println(dp[N-1][Integer.parseInt(st.nextToken())]);
	}
}

// 백트래킹으로는 시간초과 날 수밖에 없음 => dp
// 한칸씩 보는데 숫자를 모두 볼수 없을끼? => dp = new long[N][21]
// 범위 내의 값에 대해 계속 더해주면 됨