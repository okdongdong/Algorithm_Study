import java.io.BufferedReader;
import java.io.InputStreamReader;

class boj16946 {
  public static void main(String args[]) throws Exception {
    BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));

    int[][] arr = new int[1000][1000];
    int[][] wall_arr = new int[1000][1000];

    boolean[][] visited = new boolean[1000][1000];
    String[] NM = sc.readLine().split(" ");
    int N = Integer.parseInt(NM[0]);
    int M = Integer.parseInt(NM[1]);
    int nr, nc, rr, cc;
    int[] dr = { 0, 0, 1, -1 };
    int[] dc = { 1, -1, 0, 0 };
    int[][] stack = new int[1000000][2];
    int[][] wall_list = new int[1000000][2];
    StringBuilder result = new StringBuilder();

    // 배열입력
    for (int r = 0; r < N; r++) {
      String[] temp = sc.readLine().split("");
      for (int c = 0; c < M; c++) {
        arr[r][c] = Integer.parseInt(temp[c]);
      }
    }

    // 원래 갈수 있는 곳 개수 체크
    for (int r = 0; r < N; r++) {
      for (int c = 0; c < M; c++) {

        if (visited[r][c] || arr[r][c] == 1) {
          continue;
        } else {
          int head = 0;
          int tail = 0;
          int idx = 0;
          int cnt = 1;
          stack[tail][0] = r;
          stack[tail++][1] = c;
          visited[r][c] = true;
          while (head < tail) {

            rr = stack[head][0];
            cc = stack[head++][1];

            for (int i = 0; i < 4; i++) {

              nr = rr + dr[i];
              nc = cc + dc[i];

              if (0 <= nr && nr < N && 0 <= nc && nc < M ) {
                if (!visited[nr][nc]) {
                if (arr[nr][nc] == 0) {
                  stack[tail][0] = nr;
                  stack[tail++][1] = nc;
                  cnt++;
                } else {
                  wall_list[idx][0] = nr;
                  wall_list[idx++][1] = nc;
                }
                visited[nr][nc] = true;
              }
            }
            }
          }

          for (int i = 0; i < idx; i++) {
            rr = wall_list[i][0];
            cc = wall_list[i][1];
            wall_arr[rr][cc] += cnt;
            visited[rr][cc] = false;
          }
        }
      }
    }

    // 벽부수고 가는 곳 체크
    for (int r = 0; r < N; r++) {
      for (int c = 0; c < M; c++) {
        if (arr[r][c] == 0) {

          result.append("0");

        } else {

          result.append((wall_arr[r][c]+1)%10);

        }
      }
      result.append("\n");
    }
    System.out.println(result);
    sc.close();
  }
}