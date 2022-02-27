import java.util.Scanner;

class Main
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		
		int A, B;

		while (true) {
			A = sc.nextInt();
			B = sc.nextInt();
			if (A == 0 && B==0) {
				break;
			}
			if (A>B) {
				System.out.println("Yes");
			} else {
				System.out.println("No");
			}
			
		}
				
		sc.close();
	}
}