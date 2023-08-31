import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N, M, ans;
	static int[][] board, dp;
    static boolean[][] visited;    
	static int[] dx = { 0, 0, -1, 1 };
	static int[] dy = { -1, 1, 0, 0 };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		board = new int[N][M];
		dp = new int[N][M];
        visited= new boolean[N][M];
        ans =0;
		for (int i = 0; i < N; i++) {
			String str = br.readLine();
			for (int j = 0; j < M; j++) {
				if (str.charAt(j) == 'H')
					board[i][j] = -1;
				else
					board[i][j] = str.charAt(j) - '0';
			}
		}
        visited[0][0]=true;
		dfs(0, 0, 0);

        System.out.println(ans);
	}

	static void dfs(int x, int y, int cnt) {
		ans = Math.max(ans, cnt+1);
		dp[x][y] = cnt+1;
		int val = board[x][y];
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i] * val;
			int ny = y + dy[i] * val;

			if (nx < 0 || ny < 0 || nx >= N || ny >= M ||board[nx][ny] == -1) {
				continue;
			}
            if(visited[nx][ny]){
                System.out.println(-1);
                System.exit(0);
            }
            if(dp[nx][ny]>cnt+1) continue;
            visited[nx][ny]=true;
			dfs(nx, ny, cnt + 1);
            visited[nx][ny]=false;
		}
	}

}
