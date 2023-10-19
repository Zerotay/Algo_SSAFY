// 18870 좌표압축 (S2)
// https://www.acmicpc.net/problem/18870
// 성공
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
  public static void main(String[] args) throws IOException {
    StringTokenizer st;
    StringBuilder sb = new StringBuilder();
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    HashMap<Integer, Integer> rankMap = new HashMap<Integer, Integer>();

    int[] org = new int[N];
    int[] sorted = new int[N];
    st = new StringTokenizer(br.readLine(), " ");
    for (int i = 0; i < N; i++) {
      org[i] = sorted[i] = Integer.parseInt(st.nextToken());
    }
    Arrays.sort(sorted);
    int rank = 0;
    for (int i : sorted) {
      if (!rankMap.containsKey(i)) {
        rankMap.put(i, rank);
        rank++;
      }
    }
    for (int i : org) {
      sb.append(rankMap.get(i)).append(" ");
    }
    System.out.println(sb);
  }
}