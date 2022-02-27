import java.util.Scanner;

class boj10870
{
	
	public static int fibo(int num) {
		if (num<2) {
			return num;
		} else {
			return fibo(num-2) + fibo(num-1);
		}
	}
	
	
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();	
		int result = fibo(n);
		
		System.out.println(result);
		
		sc.close();
	}
}