import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        
        for (int t = 0; t < T; t++) {
            boolean flag = false;
            Stack<Character> stk = new Stack<>();
            String s = br.readLine();
            
            for (int i = 0; i < s.length(); i++) {
                char ch = s.charAt(i);
                
                if (ch == '(') {
                    stk.push(ch);
                } else if (ch == ')') {
                    if (!stk.isEmpty()) {
                        if (stk.peek() == '(') {
                            stk.pop();
                        } else if (stk.peek() == ')') {
                            stk.push(ch);
                        } else if (stk.peek() == '?') {
                            stk.pop();
                        }
                    } else {
                        flag = true;
                        break;
                    }
                } else if (ch == '?') {
                    if (!stk.isEmpty()) {
                        if (stk.peek() == '(') {
                            stk.pop();
                        } else if (stk.peek() == ')') {
                            stk.push(ch);
                        } else if (stk.peek() == '?') {
                            stk.push(ch);
                        }
                    } else {
                        stk.push('?');
                    }
                } else if (ch == '*') {
                    if (!stk.isEmpty()) {
                        while (!stk.isEmpty()) {
                            if (stk.peek() == ')') {
                                break;
                            }
                            stk.pop();
                        }
                        stk.push(ch);
                    } else {
                        stk.push(ch);
                    }
                }
            }
            
            if (flag) {
                System.out.println("No");
            } else {
                if (stk.isEmpty()) {
                    System.out.println("Yes");
                }
                    if (stk.size() == 1 && stk.peek() == '*') {
                        System.out.println("YES");
                    } else {
                        System.out.println("NO");
                    }
                
            }
        }
    }
}