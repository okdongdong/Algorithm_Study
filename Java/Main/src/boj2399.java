import java.io.BufferedReader;
import java.io.InputStreamReader;

class boj2399 {
  public static void main(String args[]) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    String[] nums = br.readLine().split(" ");
    long result = 0;
    for (int i = 0; i < N - 1; i++) {
      for (int j = i + 1; j < N; j++) {
        int x = Integer.parseInt(nums[i]);
        int y = Integer.parseInt(nums[j]);
        result += Math.abs(x - y);
      }
    }
    System.out.println(result*2);
    br.close();
  }
}
