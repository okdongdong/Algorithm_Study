import java.io.BufferedReader;
import java.io.InputStreamReader;


class boj10828 
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in)); //선언
		
		int N = Integer.parseInt(bf.readLine());
		int[] nums = new int[10000];
		String result = "";
		int idx = -1;
		
		for (int i=0; i<N; i++) {
			String cmds[] = bf.readLine().split(" ");
			String cmd =  cmds[0];

			switch(cmd){
			
			case "push":
				int num = Integer.parseInt(cmds[1]);
				idx++;
				nums[idx] = num;
				break;
				
			case "pop":
				if (idx < 0) {
					result += "-1\n";
				} else {
					result += nums[idx] + "\n";
					--idx;
					}
				break;
				
			case "size":
				int size = idx+1;
				result += size + "\n";
				break;
				
			case "empty":
				if (idx < 0) {
					result += "1\n";
				} else {
					result += "0\n";
				}
				break;
				
			case "top":
				if (idx < 0) {
					result += "-1\n";
				} else {
					result += nums[idx] + "\n";
				}
				break;
			}
		}
		System.out.println(result);
		bf.close();
	}
}
	