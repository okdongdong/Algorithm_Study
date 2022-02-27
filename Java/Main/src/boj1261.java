import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class boj1261 {
  public static void main(String args[]) throws Exception {
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    int[][] arr = new int[100][100];
    int[][] moveCnt = new int[100][100];
    String[] NM = bf.readLine().split(" ");
    int N = Integer.parseInt(NM[0]);
    int M = Integer.parseInt(NM[1]);
    int[] dr = { 0, 0, 1, -1 };
    int[] dc = { 1, -1, 0, 0 };

    // 배열 입력
    for (int r = 0; r < M; r++) {
      String[] temp = bf.readLine().split("");
      for (int c = 0; c < N; c++) {
        arr[r][c] = Integer.parseInt(temp[c]);
        moveCnt[r][c] = 99999;
      }
    }

    // 최소 벽 카운트
    Queue<Integer> rQue = new LinkedList<>();
    Queue<Integer> cQue = new LinkedList<>();

    rQue.add(0);
    cQue.add(0);

    int r, c, nr, nc;

    moveCnt[0][0] = 0;

    while (rQue.size() > 0) {
      r = rQue.poll();
      c = cQue.poll();

      for (int i = 0; i < 4; i++) {
        nr = r + dr[i];
        nc = c + dc[i];
        if (0 <= nr && nr < M && 0 <= nc && nc < N) {

          if (arr[nr][nc] == 1) { // 벽을 부수고 이동해야할 때

            if (moveCnt[r][c] + 1 < moveCnt[nr][nc]) {
              moveCnt[nr][nc] = moveCnt[r][c] + 1;
              rQue.add(nr);
              cQue.add(nc);
            }

          } else { // 벽을 안부수고 이동할 때

            if (moveCnt[r][c] < moveCnt[nr][nc]) {
              moveCnt[nr][nc] = moveCnt[r][c];
              rQue.add(nr);
              cQue.add(nc);
            }
          }
        }
      }
    }
    System.out.println(moveCnt[M-1][N-1]);
    bf.close();
  }
}
