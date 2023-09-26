import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static char[][] map;
	static int[][][] visited;

	static int[] dx = { 0, 0, -1, 1 };
	static int[] dy = { -1, 1, 0, 0 };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		int[] startpoint = new int[2];
		map = new char[N][M];

		for (int i = 0; i < N; i++) {
			String str = br.readLine();
			for (int j = 0; j < M; j++) {
				map[i][j] = str.charAt(j);
				if (map[i][j] == '0') {
					startpoint[0] = i;
					startpoint[1] = j;
				}
			}
		}
		visited = new int[N][M][64];
		System.out.println(bfs(startpoint[0], startpoint[1]));
	}

	private static int bfs(int x, int y) {
		Queue<int[]> q = new ArrayDeque<int[]>();
		int ori_key = 0;
		visited[x][y][ori_key] = 1;
		q.add(new int[] { x, y, ori_key });

		int ans = -1;
		int move = 1;
		while (!q.isEmpty()) {
			int size = q.size();

			for (int i = 0; i < size; i++) {
				int[] tmp = q.poll();
				x = tmp[0];
				y = tmp[1];
				ori_key = tmp[2];

				if (map[x][y] == '1') {
					return move - 1;
				}

				for (int j = 0; j < 4; j++) {
					int nx = x + dx[j];
					int ny = y + dy[j];
					int key = ori_key;

					if (nx < 0 || ny < 0 || nx >= N || ny >= M || map[nx][ny] == '#' || visited[nx][ny][key] == 1)
						continue;

					if (map[nx][ny] >= 'a' && map[nx][ny] <= 'f') {
						visited[nx][ny][key |= 1 << (map[nx][ny] - 'a')] = 1;
						q.add(new int[] { nx, ny, key |= 1 << (map[nx][ny] - 'a') });
					} else {
						visited[nx][ny][key] = 1;
						if (map[nx][ny] >= 'A' && map[nx][ny] <= 'F' && (key & (1 << (map[nx][ny] - 'A'))) == 0)
							continue;
						q.add(new int[] { nx, ny, key });
					}
//					System.out.println(nx + " " + ny + " " + key + " "  + move);
				}
			}
			move++;
		}
		return ans;
	}
}
