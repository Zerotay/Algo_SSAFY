package alg;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

public class G1941 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static char[][] map = new char[5][5];
	static int[][] idx = new int[5][5];
	static int[][] visited;
	static int[] pick = new int[7];
	static int[] dx = { 0, 0, -1, 1 };
	static int[] dy = { -1, 1, 0, 0 };
	static int ans;

	public static void main(String[] args) throws IOException {
		int cnt = 0;

		for (int i = 0; i < 5; i++) {
			char[] str = br.readLine().toCharArray();
			for (int j = 0; j < 5; j++) {
				map[i][j] = str[j];
				idx[i][j] = cnt++;
			}
		}
		comb(0, 0);
		System.out.println(ans);
	}

	static void comb(int dep, int flag) {
		if (dep == 7) {
			visited = new int[5][5];
			bfs();
			return;
		}
		for (int i = flag; i < 25; i++) {
			pick[dep] = i;
			comb(dep + 1, i + 1);
		}
	}

	private static void bfs() {
		Queue<int[]> q = new ArrayDeque<>();
		int cnt = 0;
		for (int i = 0; i < 7; i++) {
			int x = pick[i] / 5;
			int y = pick[i] % 5;
			visited[x][y] = 1;
			if (map[x][y] == 'S')
				cnt++;
			else
				cnt--;
		}
		if (cnt < 1)
			return;
		cnt = 1;
		int x = pick[0] / 5;
		int y = pick[0] % 5;
		q.offer(new int[] { x, y });
		visited[x][y]=2;
		while (!q.isEmpty()) {
			int[] xy = q.poll();
			for (int i = 0; i < 4; i++) {
				int nx = xy[0] + dx[i];
				int ny = xy[1] + dy[i];
				if (nx < 0 || ny < 0 || nx >= 5 || ny >= 5)
					continue;
				if(visited[nx][ny]==1) {
					visited[nx][ny]+=1;
					cnt+=1;
					q.offer(new int[] {nx,ny});
				}
			}
		}
		if(cnt!=7) return;
		ans+=1;
	}
}
