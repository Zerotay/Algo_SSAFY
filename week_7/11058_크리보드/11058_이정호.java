// 11058 크리보드(G5)
// https://www.acmicpc.net/problem/11058
// 정답

public class Main {
  public static void main(String[] args) throws Exception {
        int N = read();
        long[] dp = new long[N+1];
        
        if (N < 7) {
            dp[N] = N;
        } else {
            dp[3] = 3;
            dp[4] = 4;
            dp[5] = 5;
            dp[6] = 6;
            for (int i = 7; i <= N; i++) {
                for (int j = 3; j <= i; j++) {
                    dp[i] = Math.max(dp[i], dp[i - j] * (j - 1));
                }
            }
        }
        System.out.println(dp[N]);
    }
    
    private static int read() throws Exception {
        int c, n = System.in.read() & 15;
        while ((c = System.in.read()) > 32) n = (n << 3) + (n << 1) + (c  & 15);
        if (c == 13) System.in.read();
        return n;
    }
}
