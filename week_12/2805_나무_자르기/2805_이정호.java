// 2805 나무 자르기 (S2)
// https://www.acmicpc.net/problem/2805
// 정답

public class Main {
  public static void main(String[] args) throws Exception {
    int N = read();
    int M = read();
    int ans = 0;
    int max = 0;
    int tmp = N;
    int arr[] = new int[N];
    while (--tmp >= 0) {
      arr[tmp] = read();
      max = Math.max(max, arr[tmp]);
    }
    int mid;
    long sum;
    while (ans < max) {
      mid = (ans + max) / 2;
      sum = 0;
      for (int height : arr) {
        if (height > mid) {
          sum += height - mid;;
        }
      }

      if (sum < M) {
        max = mid;
      } else {
        ans = mid + 1;
      }
    }
    System.out.println(ans - 1);
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