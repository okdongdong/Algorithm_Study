import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class boj17281 {

  public static int cnt = 0;

  public static void permutation(int[] arr, int[][] result, int depth) {
    if (depth == 8) {
      for (int idx = 0; idx < 9; idx++) {

        result[cnt][idx] = arr[idx];
      }
      cnt++;
      return;
    }

    for (int i = depth; i < 9; i++) {
      if (i == 3) {
        continue;
      }

      swap(arr, depth, i);
      if (depth == 2) {
        permutation(arr, result, depth + 2);
      } else {
        permutation(arr, result, depth + 1);
      }
      swap(arr, depth, i);
    }

  }

  public static void swap(int[] arr, int depth, int i) {
    int temp = arr[depth];
    arr[depth] = arr[i];
    arr[i] = temp;
  }

  public static void main(String args[]) throws Exception {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int[][] arr = new int[N][9];
    int player_order_cnt = 1;
    for (int i = 1; i < 9; i++) {
      player_order_cnt *= i;
    }
    int[] order = { 1, 2, 3, 0, 4, 5, 6, 7, 8 };
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < 9; j++) {
        arr[i][j] = sc.nextInt();
      }
    }
    int[][] player_order = new int[player_order_cnt][9];

    permutation(order, player_order, 0);

    int max_score = 0;
    int idx, score, out_cnt, now_player, hitball;
    Queue<Boolean> field = new LinkedList<>();

    for (int i = 0; i < player_order_cnt; i++) {
      idx = 0;
      score = 0;

      for (int inning = 0; inning < N; inning++) {
        out_cnt = 0;
        field.clear();
        field.add(false);
        field.add(false);
        field.add(false);

        while (out_cnt < 3) {
          now_player = player_order[i][idx];
          hitball = arr[inning][now_player];
          if (hitball == 0) {
            out_cnt++;
          } else {
            for (int hitman = 0; hitman < hitball; hitman++) {
              if (hitman == 0) {
                field.add(true);
              } else {
                field.add(false);
              }
              if (field.poll()) {
                score++;
              }
            }
          }
          idx++;
          if (idx == 9) {
            idx = 0;
          }
        }
      }
      if (max_score < score) {
        max_score = score;
      }
    }
    System.out.println(max_score);
    sc.close();
  }

}
