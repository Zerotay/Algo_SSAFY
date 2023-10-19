// 20529 가장 가까운 세 사람의 심리적 거리 (S1)
// https://www.acmicpc.net/problem/20529
// 정답

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  public static void main(String[] args) throws NumberFormatException, IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    int T = Integer.parseInt(br.readLine());
    StringBuilder sb = new StringBuilder();
    int N, tmp, ans;
    String[] s;
    while (T-- > 0) {
      N = Integer.parseInt(br.readLine());
      st = new StringTokenizer(br.readLine(), " ");
      if (N > 47) {
        sb.append(0).append("\n");
      } else {
        ans = 12;
        s = new String[N];
        for (int i = 0; i < N; i++) {
          s[i] = st.nextToken();
        }

        loop: for (int i = 0; i < N; i++) {
          for (int j = 0; j < N; ++j) {
            for (int k = 0; k < N; ++k) {
              if (i == j || j == k || k == i)
                continue;
              tmp = 0;
              for (int l = 0; l < 4; l++) {
                tmp += (s[i].charAt(l) != s[j].charAt(l) ? 1 : 0);
                tmp += (s[j].charAt(l) != s[k].charAt(l) ? 1 : 0);
                tmp += (s[i].charAt(l) != s[k].charAt(l) ? 1 : 0);
              }
              ans = Math.min(ans, tmp);
              if (ans == 0) {
                break loop;
              }
            }
          }
        }
        sb.append(ans).append("\n");
      }
    }
    System.out.println(sb);
  }
}