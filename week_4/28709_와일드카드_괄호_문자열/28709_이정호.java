import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
    static String line;
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            line = br.readLine();
            if(isGood()){
                sb.append("YES\n");
                continue;
            }
            sb.append("NO\n");
        }
        System.out.print(sb.toString());
    }

    public static boolean isGood() {
        char[] chars = line.toCharArray();
        int countStar = 0;
        for (char c : chars) {
            if (c == '*') {
                countStar++;
            }
        }
        if (countStar >= 1) {
            int cnt = 0;
            for (char c : chars) {
                if (c == '*') {
                    break;
                }
                if (c == ')') {
                    cnt--;
                } else {
                    cnt++;
                }
                if (cnt < 0) {
                    return false;
                }
            }
            cnt = 0;
            for (int i = chars.length - 1; i >= 0; i--) {
                char c = chars[i];
                if (c == '*') {
                    break;
                }
                if (c == '(') {
                    cnt--;
                } else {
                    cnt++;
                }
                if (cnt < 0) {
                    return false;
                }
            }
            return true;
        }
        if (chars.length % 2 != 0) {
            return false;
        }
        int open = 0;
        int close = 0;
        for (char c : chars) {
            if (c == '(') {
                open++;
            } else if (c == ')') {
                close++;
            }
        }
        if (open > chars.length / 2 || close > chars.length / 2) {
            return false;
        }
        int cnt = 0;
        for (char c : chars) {
            if (c == '?') {
                if (open < chars.length / 2) {
                    c = '(';
                    open++;
                } else {
                    c = ')';
                }
            }
            if (c == '(') {
                cnt++;
            } else {
                cnt--;
            }
            if (cnt < 0) {
                return false;
            }
        }

        return true;
    }
}