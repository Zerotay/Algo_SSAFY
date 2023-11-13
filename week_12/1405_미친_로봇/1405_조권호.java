// 1405 미친 로봇 (G4)
// https://www.acmicpc.net/problem/1405
// 정답

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static double[] property;
	static double result;
	static boolean[][] visited;
	static int[] dx = { 0, 0, 1, -1 };
	static int[] dy = { 1, -1, 0, 0 };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		N = Integer.parseInt(st.nextToken());

		property = new double[4];
		for (int i = 0; i < 4; i++) {
			property[i] = Integer.parseInt(st.nextToken()) * 0.01;
		}

		visited = new boolean[29][29];
		result = 0;
		dfs(0, 14, 14, N, 1);
		System.out.printf("%.18f",result);
//		sb.append(result);
//		System.out.println(sb.toString());
	}

	public static void dfs(int dep, int x, int y, int n, double cnt) {
		if (dep == n) {
			result += cnt;
			return;
		}

		visited[x][y] = true;
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx < 0 || ny < 0 || nx >= 29 || ny >= 29 || visited[nx][ny])
				continue;

			visited[nx][ny] = true;
			dfs(dep + 1, nx, ny, n, cnt * property[i]);
			visited[nx][ny] = false;
		}
	}
}

// 그냥 DFS로 쭉 도는데 처음에 4^14까지 가는 줄 알았는데 visit 체크를 해줘도 시간초가 날 줄 알았는데 됨..
