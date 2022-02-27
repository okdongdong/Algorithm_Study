import java.io.BufferedReader;
import java.io.InputStreamReader;

class boj10845 {
  public static void main(String args[]) throws Exception
  {

    BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(sc.readLine());
    int[] que = new int[10000];
    int head = 0;
    int tail = 0;
    StringBuilder result = new StringBuilder();

    for (int n=0; n<N; n++) {
      String[] cmd = sc.readLine().split(" ");
      
      switch (cmd[0]) {
        case "push" :
          que[tail++] = Integer.parseInt(cmd[1]);
          break;
        
        case "pop":
          if (head == tail) {
            result.append("-1\n");
          } else {
            result.append(que[head++] + "\n");
          } break;

        case "size":
          result.append((tail - head) + "\n");
          break;
        
        case "empty":
          if (head == tail) {
            result.append("1\n");
          } else {
            result.append("0\n");
          } break;
          
        case "front":
          if (head == tail) {
            result.append("-1\n");
          } else {
            result.append(que[head] + "\n");
          } break;
          
        case "back":
          if (head == tail) {
            result.append("-1\n");
          } else {
            result.append(que[tail-1] + "\n");
          } break;
      }
    }
    System.out.println(result);
    sc.close();
  }
}
