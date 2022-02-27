import java.io.BufferedReader;
import java.io.InputStreamReader;

class boj9012 {
  public static void main(String args[]) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int T = Integer.parseInt(br.readLine());
    StringBuilder result = new StringBuilder();

    for (int tc = 0; tc < T; tc++) {
      int top = 0;
      String[] ps = br.readLine().split("");
      boolean flag = true;

      for (int i = 0; i < ps.length; i++) {
        if (ps[i].equals("(")) {
          top++;

        } else {

          if (top == 0) {
            result.append("NO\n");
            flag = false;
            break;

          } else {
            top--;

          }
        }
      }
      if (flag) {
        if (top == 0) {
          result.append("YES\n");

        } else {
          result.append("NO\n");
        }
      }
    }
    System.out.println(result);
  }
}
