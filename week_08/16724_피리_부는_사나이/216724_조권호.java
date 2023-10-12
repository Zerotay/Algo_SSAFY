# 16724 피리 부는 사나이(G3)
# https://www.acmicpc.net/problem/16724
# 정답

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int ans;
	static int[][] map;
	static boolean[][] visited;
	static boolean[][] check;
	static int[] dx = { 0, 0, -1, 1 };
	static int[] dy = { -1, 1, 0, 0 };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		map = new int[N][M];
		visited = new boolean[N][M];
		check = new boolean[N][M];

		for (int i = 0; i < N; i++) {
			String str = br.readLine();
			for (int j = 0; j < M; j++) {
				int command = str.charAt(j);
				if (command == 'L')
					map[i][j] = 0;
				else if (command == 'R')
					map[i][j] = 1;
				else if (command == 'U')
					map[i][j] = 2;
				else if (command == 'D')
					map[i][j] = 3;
			}
		}
		ans = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (!visited[i][j]) {
					visited[i][j] = true;
					dfs(i, j);
				}
			}
		}
		System.out.println(ans);
	}

	private static void dfs(int x, int y) {
		int nx = x + dx[map[x][y]];
		int ny = y + dy[map[x][y]];

		if (!visited[nx][ny]) {
			visited[nx][ny] = true;
			dfs(nx, ny);
		}
		else {
			if(!check[nx][ny]) ans++;
		}
		check[x][y]=true;

	}

}

// BFS로 경우 나눠서 풀면 되는데 주변 둘러보고 나한테 들어오거나 내가 나가는 것들을 체크해서 큐에 넣어주고 bfs 실행할 때마다 카운팅해주면 된다=>경우 나누기 귀찮음
// 서로소로 하려니깐 parents 만드는게 힘들거 같음 => DFS 하는데 시작하는 위치에 따라서 답이 달라질 수 있어서 연결되었을 때 마지막 값 체크
