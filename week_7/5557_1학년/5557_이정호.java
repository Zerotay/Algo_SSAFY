// 5557 1학년(G5)
// https://www.acmicpc.net/problem/5557
// 정답

public class Main {
   public static void main(String[] args) throws Exception {
        int N = read();
        long[][] dp = new long[N + 1][21];
        int[] arr = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            arr[i] = read();
        }
        
        dp[1][arr[1]] = 1;

        for (int i = 2; i <= N - 1; i++) {
            for (int j = 0; j <= 20; j++) {
                if (dp[i - 1][j] == 0)
                    continue;

                if (j + arr[i] <= 20) {
                    dp[i][j + arr[i]] += dp[i - 1][j];
                }
                if (j - arr[i] >= 0) {
                    dp[i][j - arr[i]] += dp[i - 1][j];
                }
            }
        }
        System.out.println(dp[N-1][arr[N]]);
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
