import java.util.HashMap;
import java.util.Scanner;
import java.util.Stack;

public class boj3954 {
  public static void main(String args[]) throws Exception {
    Scanner sc = new Scanner(System.in);

    int T = sc.nextInt();
    for (int tc = 0; tc < T; tc++) {
      int S_m = sc.nextInt();
      int S_c = sc.nextInt();
      int S_i = sc.nextInt();
      int[] arr = new int[S_m];
      String[] cmd_list = sc.next().split("");
      String txt = sc.next();

      HashMap<Integer, Integer> jump_dict = new HashMap<>();
      Stack<Integer> jump_stack = new Stack<>();
      for (int idx = 0; idx < S_c; idx++) {
        if (cmd_list[idx].equals("[")) {
          jump_stack.push(idx);
        } else if (cmd_list[idx].equals("]")) {
          int left_idx = jump_stack.pop();
          jump_dict.put(idx, left_idx);
          jump_dict.put(left_idx, idx);
        }
      }

      int cnt = 0;
      int idx = 0;
      int left_idx, right_idx;
      int txt_idx = 0;
      int loop_idx = 0;
      int pointer = 0;
      Boolean is_infinite = false;
      String result = "Terminates";

      while (idx < S_c) {
        if (cnt >= 50000000) {
          is_infinite = true;
          break;
        }

        switch (cmd_list[idx]) {
          case "-":
            arr[pointer] -= 1;
            arr[pointer] %= 256;
            break;

          case "+":
            arr[pointer] += 1;
            arr[pointer] %= 256;
            break;

          case "<":
            pointer--;
            break;

          case ">":
            pointer++;
            break;

          case "[":
            if (arr[pointer] == 0) {
              left_idx = jump_dict.get(idx);
              idx = left_idx;
            }
            break;

          case "]":
            if (arr[pointer] != 0) {
              right_idx = jump_dict.get(idx);
              idx = right_idx;
            }
            break;

          case ".":
            break;

          case ",":
            if (txt_idx >= S_i) {
              arr[pointer] = 255;
            } else {
              arr[pointer] = (int) txt.charAt(txt_idx++);
            }
            break;

        }
        cnt++;
        idx++;
        if (pointer < 0) {
          pointer += S_m;
        }
        pointer %= S_m;
      }

      if (is_infinite) {
        for (int i = 0; i < 50000000; i++) {
          switch (cmd_list[idx]) {
            case "-":
              arr[pointer] -= 1;
              arr[pointer] %= 256;
              break;

            case "+":
              arr[pointer] += 1;
              arr[pointer] %= 256;
              break;

            case "<":
              pointer--;
              break;

            case ">":
              pointer++;
              break;

            case "[":
              if (arr[pointer] == 0) {
                left_idx = jump_dict.get(idx);
                idx = left_idx;
              }
              break;

            case "]":
              if (arr[pointer] != 0) {

                if (loop_idx < idx) {
                  loop_idx = idx;
                }

                right_idx = jump_dict.get(idx);
                idx = right_idx;
              }
              break;

            case ".":
              break;

            case ",":
              if (txt_idx >= S_i) {
                arr[pointer] = 255;
              } else {
                arr[pointer] = (int) txt.charAt(txt_idx++);
              }
              break;

          }
          idx++;
          if (pointer < 0) {
            pointer += S_m;
          }
          pointer %= S_m;

        }

        result = "Loops " + jump_dict.get(loop_idx) + " " + loop_idx;
      }
      System.out.println(result);

    }
    sc.close();
  }
}
