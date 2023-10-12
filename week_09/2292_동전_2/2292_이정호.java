import java.util.Arrays;

public class Main{
    public static void main(String[] args) throws Exception {
        int n = read();
        int k = read();

        int[] coin = new int[n];
        int[] dp = new int[k + 1];
		dp[0] = 0;

        Arrays.fill(dp, 100001);
        for (int i = 0; i < n; i++) {
            coin[i] = read();
        }

        for (int i = 0; i < n; i++) {
            for (int j = coin[i]; j < k + 1; j++) {
                dp[j] = Math.min(dp[j], dp[j - coin[i]] + 1);
            }
        }
        if (dp[k] == 100001)
            System.out.println(-1);
        else
            System.out.println(dp[k]);
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