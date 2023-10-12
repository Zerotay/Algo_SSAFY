// 1103 게임 (G2)
// https://www.acmicpc.net/problem/1103
// 성공

package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main_1103_G2_게임_이정호 {
    private static int N, M;
    private static char[][] graph;
    private static int[][] dp;
    private static boolean[][] visited;
    private static int tmp;
    private static int[] dx = { 0, 1, 0, -1 };
    private static int[] dy = { 1, 0, -1, 0 };

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = read();
        M = read();
        graph = new char[N][M];
        dp = new int[N][M];
        visited = new boolean[N][M];

        String line;
        for (int i = 0; i < N; i++) {
            line = br.readLine();
            Arrays.fill(dp[i], -1);
            graph[i] = line.toCharArray();
        }
        System.out.println(dfs(0, 0) + 1);
    }

    private static int dfs(int r, int c) {
        if (visited[r][c]) {
            System.out.println(-1);
            System.exit(0);
        }
        if (dp[r][c] > -1) {
            return dp[r][c];
        }
        visited[r][c] = true;
        dp[r][c] = 0;
        int nr, nc, len;
        for (int i = 0; i < 4; i++) {
            len = graph[r][c] - '0';
            nr = r + len * dx[i];
            nc = c + len * dy[i];
            if (nr < 0 || nr >= N || nc < 0 || nc >= M || graph[nr][nc] == 'H')
                continue;
            tmp = dfs(nr, nc) + 1;
            dp[r][c] = tmp > dp[r][c] ? tmp : dp[r][c];
            visited[nr][nc] = false;
        }
        return dp[r][c];
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