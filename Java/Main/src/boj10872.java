import java.io.BufferedReader;
import java.io.InputStreamReader;

class boj10872 {

  public static int factorial(int n) {
    if (n < 2) {
      return 1;
    } else {
      return factorial(n - 1) * n;
    }
  }

  public static void main(String args[]) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    System.out.println(factorial(N));

  }
}
