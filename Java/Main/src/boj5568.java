import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

class boj5568 {
  static Set<String> nums = new HashSet<String>(); // 전역변수로 설정

  public static void makeNumber(int k, int cnt, int[] cards, boolean[] checkArr, String num) throws Exception {
    if (k == cnt) {
      nums.add(num);
      return;
    }
    for (int i = 0; i < cards.length; i++) {
      if (checkArr[i]) {
        continue;
      }
      checkArr[i] = true;
      makeNumber(k , cnt+1, cards, checkArr, num + String.valueOf(cards[i]));
      checkArr[i] = false;
    }

    return;
  }

  public static void main(String args[]) throws Exception {
    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();
    int k = sc.nextInt();
    boolean[] checkArr = new boolean[n];
    int[] cards = new int[n];
    for (int i = 0; i < n; i++) {
      cards[i] = sc.nextInt();
    }

    makeNumber(k, 0, cards, checkArr, "");

    System.out.println(nums.size());
    sc.close();
  }
}