// 14500 테트로미노 (G4)
// https://www.acmicpc.net/problem/14500
// 정답

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static StringTokenizer st;
	static int N, M, ans;
	static int[][] map;
	static boolean[][] visited;
	static int[] dx = { 0, 0, -1, 1 };
	static int[] dy = { -1, 1, 0, 0 };

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		map = new int[N][M];
		visited = new boolean[N][M];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		ans = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				visited[i][j] = true;
				dfs(i, j, 0, map[i][j]);
				visited[i][j] = false;
			}
		}
		sb.append(ans);
		System.out.println(sb.toString());
	}

	private static void dfs(int i, int j, int dep, int cnt) {
		if (dep == 3) {
			ans = Math.max(ans, cnt);
			return;
		}
		for (int k = 0; k < 4; k++) {
			int nx = i + dx[k];
			int ny = j + dy[k];
			
			if (nx < 0 || ny < 0 || nx >= N || ny >= M || visited[nx][ny])
				continue;
			if(dep==1) {
				visited[nx][ny] = true;
				dfs(i, j, dep + 1,  cnt + map[nx][ny]);
				visited[nx][ny] = false;
			}
			visited[nx][ny] = true;
			dfs(nx, ny, dep + 1,  cnt + map[nx][ny]);
			visited[nx][ny] = false;
		}
	}
}
