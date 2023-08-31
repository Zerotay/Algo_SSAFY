import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static int[][] map;
	static long[][] sum;
	static long ans;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		map = new int[N + 1][M + 1];

		for (int i = 0; i < N; i++) {
			String str = br.readLine();
			for (int j = 0; j < M; j++) {
				map[i + 1][j + 1] = str.charAt(j) - '0';
			}
		}

		sum = new long[N + 1][M + 1];
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= M; j++) {
				sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + (long) map[i][j];
			}
		}

		ans = 0;
		for (int i = 1; i <= N - 2; i++) { // ---
			for (int j = i + 1; j <= N - 1; j++) {
				long one = sum[i][M] - sum[i][0] - sum[0][M] + sum[0][0];
				long two = sum[1][M] - sum[1][0] - sum[i][M] + sum[i][0];
				long three = sum[N][M] - sum[N][0] - sum[j][M] + sum[j][0];
				ans = Math.max(ans, one * two * three);
			}
		}

		for (int i = 1; i <= M - 2; i++) { // |||
			for (int j = i + 1; j <= M - 1; j++) {
				long one = sum[N][i] - sum[N][0] - sum[0][i] + sum[0][0];
				long two = sum[N][j] - sum[N][i] - sum[0][i + 1] + sum[0][i];
				long three = sum[N][M] - sum[N][j] - sum[0][M] + sum[0][j];
				ans = Math.max(ans, one * two * three);
			}
		}

		for (int i = 1; i <= N - 1; i++) { 
			for (int j = 1; j <= M - 1; j++) {
				long one = sum[N][j] - sum[N][0] - sum[0][j] + sum[0][0];
				long two = sum[i][M] - sum[i][j] - sum[0][M] + sum[0][j];
				long three = sum[N][M] - sum[N][j] - sum[i][M] + sum[0][0];
				ans = Math.max(ans, one * two * three);
				
				one = sum[i][j] - sum[i][0] - sum[0][j] + sum[0][0];
				two = sum[N][j] - sum[N][0] - sum[i][j] + sum[i][0];
				three = sum[N][M] - sum[N][j] - sum[0][M] + sum[0][j];
				ans = Math.max(ans, one * two * three);
				
				one = sum[i][M] - sum[i][0] - sum[0][M] + sum[0][0];
				two = sum[N][j] - sum[N][0] - sum[i][j] + sum[i][0];
				three = sum[N][M] - sum[N][j] - sum[i][M] + sum[i][j];
				ans = Math.max(ans, one * two * three);
				
				one = sum[i][j] - sum[i][0] - sum[0][j] + sum[0][0];
				two = sum[i][M] - sum[i][j] - sum[0][M] + sum[0][j];
				three = sum[N][M] - sum[N][0] - sum[i][M] + sum[i][0];
				ans = Math.max(ans, one * two * three);
			}
		}
		System.out.println(ans);
	}

}