// 테스트 케이스 개수가 주어진다.
// N : 배열의 크기
// K : 퍼지는 시간(날짜)
// K일 후 살아남은 생존자의 수를 구하자.
// 3 <= N <= 20
// ​1 <= K <= 50
// ​빈칸: 0
// ​바다: 1
// ​백신: 2
// ​바이러스: 3
// ​사람: 4

import java.util.Scanner;
import java.util.LinkedList;
import java.util.Queue;

public class solution {
  public static void main(String args[]) throws Exception {
    Scanner sc = new Scanner(System.in);
    StringBuilder sb = new StringBuilder(); // 답안을 한번에 출력하기 위한 String builder
    int T = sc.nextInt(); // 테스트 케이의 수

    for (int tc = 1; tc <= T; tc++) {
      int N = sc.nextInt(); // 배열의 크기
      int K = sc.nextInt(); // 일 수
      int man_cnt = 0; // 전체 인원 수
      int dead_man_cnt = 0; // 사망한 인원 수
      // BFS 위해 Queue 사용
      Queue<Integer> vac_r_que = new LinkedList<>(); // 백신의 r좌표를 저장할 큐
      Queue<Integer> vac_c_que = new LinkedList<>(); // 백신의 c좌표를 저장할 큐
      Queue<Integer> vir_r_que = new LinkedList<>(); // 바이러스의 r좌표를 저장할 큐
      Queue<Integer> vir_c_que = new LinkedList<>(); // 바이러스의 c좌표를 저장할 큐
      int[] dr = { 0, 0, -1, 1 }; // 4방향 탐색을 위한 좌표설정(좌우상하)
      int[] dc = { -1, 1, 0, 0 };
      int[][] arr = new int[N][N]; // N*N크기의 이차원 배열 생성
      int nr, nc; // 아래에서 다음좌표로 사용될 nr, nc 미리 선언

      // 배열 입력, 배열입력과 동시에 백신, 바이러스의 위치와 전체인원수를 카운트 한다.
      for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
          arr[i][j] = sc.nextInt();
          if (arr[i][j] == 2) {
            // 백신위치 체크
            vac_r_que.offer(i);
            vac_c_que.offer(j);

          } else if (arr[i][j] == 3) {
            // 바이러스위치 체크
            vir_r_que.offer(i);
            vir_c_que.offer(j);

          } else if (arr[i][j] == 4) {
            // 전체 인원수 체크
            man_cnt++;

          }
        }
      }

      // K일 만큼 반복
      for (int k = 0; k < K; k++) {
        // 백신 전파, 현재 가지고있는 좌표의 수만큼 큐에서 꺼내어 전파시킴
        int vac_length = vac_r_que.size();
        for (int i = 0; i < vac_length; i++) {
          int vr = vac_r_que.poll(); // 기존위치를 큐에서 꺼냄
          int vc = vac_c_que.poll();

          for (int d = 0; d < 4; d++) {
            nr = vr + dr[d];
            nc = vc + dc[d];
            // 범위체크
            if (0 <= nr && nr < N && 0 <= nc && nc < N && (arr[nr][nc] == 0 || arr[nr][nc] == 4)) {
              vac_r_que.offer(nr); // 새롭게 퍼진 위치를 큐에 다시 넣어준다.
              vac_c_que.offer(nc);

              // 백신이 퍼진 위치 값 변경
              arr[nr][nc] = 2;
            }
          }
        }
        // 바이러스 전파
        int vir_length = vir_r_que.size();
        for (int i = 0; i < vir_length; i++) {
          int vr = vir_r_que.poll();
          int vc = vir_c_que.poll();

          for (int d = 0; d < 4; d++) {
            nr = vr + dr[d];
            nc = vc + dc[d];

            if (0 <= nr && nr < N && 0 <= nc && nc < N && (arr[nr][nc] == 0 || arr[nr][nc] == 4)) {
              vir_r_que.offer(nr);
              vir_c_que.offer(nc);

              if (arr[nr][nc] == 4) {
                dead_man_cnt++;

              }
              // 바이러스가 퍼진 위치 값 변경
              arr[nr][nc] = 3;
            }
          }
        }
      }

      // 전체 인원수 - 죽은 사람수 = 생존인원 수
      sb.append(String.format("#%d %d\n", tc, man_cnt - dead_man_cnt));
    }
    System.out.print(sb.toString());

    sc.close();
  }
}
