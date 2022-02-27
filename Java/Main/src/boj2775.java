import java.util.Scanner;

class boj2775 {
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    
    int T = sc.nextInt();
    int[][] arr = new int[15][15];
    
    // 층별 인원 계산
    for (int i=0; i<15; i++) {
      arr[0][i] = i;
    }

    for (int i=1; i<15; i++) {
      for (int j=0; j<15; j++) {
        for (int l=0; l<j+1; l++) {

          arr[i][j] += arr[i-1][l];

        }
      }
    }

    // tc별 결과 출력
    for (int tc=0; tc<T; tc++) {
      int k = sc.nextInt();
      int n = sc.nextInt();
      System.out.println(arr[k][n]);
      }
    sc.close();
  }
}