// 1103 게임 (G2)
// https://www.acmicpc.net/problem/1103
// 시간초과

package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_1103_G2_게임_이정호 {
     private static int N, M;
    private static char[][] graph;
    private static boolean[][] visited;
    private static int ans = Integer.MIN_VALUE;
    private static int[] dx = { 0, 1, 0, -1 };
    private static int[] dy = { 1, 0, -1, 0 };
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = read();
        M = read();
        graph = new char[N][M];
        visited = new boolean[N][M];

        String line;
        for (int i = 0; i < N; i++) {
            line = br.readLine();
            for (int j = 0; j < M; j++) {
                graph[i][j] = line.charAt(j);
            }
        }
        dfs(0, 0, 1);
        System.out.println(ans);
    }

    private static void dfs(int r, int c, int cnt) {
        if (visited[r][c]) {
            System.out.println(-1);
            System.exit(0);
        }
        visited[r][c] = true;
        int nr, nc, len;
        for (int i = 0; i < 4; i++) {
            len = graph[r][c] - '0';
            nr = r + len * dx[i];
            nc = c + len * dy[i];
            if (nr < 0 || nr >= N || nc < 0 || nc >= M || graph[nr][nc] == 'H')
                continue;
            dfs(nr, nc, cnt + 1);
            visited[nr][nc] = false;
        }
        ans = Math.max(ans, cnt);
        return;
    }
    static int read() throws IOException {
        int c, n = System.in.read() & 15;
        while ((c = System.in.read()) > 32)
            n = (n << 3) + (n << 1) + (c & 15);
        if (c == 13)
            System.in.read();
        return n;
    }
}