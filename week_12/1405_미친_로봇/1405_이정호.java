// 1405 미친 로봇 (G4)
// https://www.acmicpc.net/problem/1405
// 성공

import java.util.Arrays;

public class Main_1405 {
  static double[] dir = new double[4];
  static boolean[][] visited;
  static int N, range;
  static int[] dx = { 0, 0, 1, -1 }; // 동 서 남 북
  static int[] dy = { 1, -1, 0, 0 };
  static double ans;

  public static void main(String[] args) throws Exception {
    N = read();
    dir[0] = read() * 0.01;
    dir[1] = read() * 0.01;
    dir[2] = read() * 0.01;
    dir[3] = read() * 0.01;
    ans = 0;
    range = N * 2 + 1;
    visited = new boolean[range][range];
    dfs(N, N, 1, 0);
    System.out.println(ans);
  }

  public static void dfs(int x, int y, double total, int depth) {
    if (depth == N) {
      ans += total;
      return;
    }
    visited[x][y] = true;

    for (int i = 0; i < 4; i++) {
      int nx = x + dx[i];
      int ny = y + dy[i];
      if (nx >= 0 && ny >= 0 && nx < range && ny < range && !visited[nx][ny]) {
        visited[nx][ny] = true;
        dfs(nx, ny, total * dir[i], depth + 1);
        visited[nx][ny] = false;
      }
    }
  }

  private static int read() throws Exception {
    int c, n = System.in.read() & 15;
    while ((c = System.in.read()) > 32)
      n = (n << 3) + (n << 1) + (c & 15);
    if (c == 13)
      System.in.read();
    return n;
  }
}

//