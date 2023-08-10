import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner scan = new Scanner(System.in);
		int a = scan.nextInt();
		double total;
		double sum;
		
		int num[][] = new int[a][];
		
		for (int i = 0; i < a; i++) {
			int point = scan.nextInt();
			num[i]= new int[point];
			
			for (int j = 0; j < num[i].length; j++) {
				num[i][j] = scan.nextInt();
			}			
			
		}
		
		
		for (int i = 0; i < a; i++) {
			
			total = 0;
			sum = 0;
			
			for (int j = 0; j < num[i].length; j++) {
				total += num[i][j];
			}
			
			for (int j = 0; j < num[i].length; j++) {
				if(num[i][j] > total / num[i].length) 
					++sum;
	
			}
			
			System.out.printf("%.3f%%\n", (sum / num[i].length) * 100);
			
		
	
		}
		
		scan.close();
	}

}
