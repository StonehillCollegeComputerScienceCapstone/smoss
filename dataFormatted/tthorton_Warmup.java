import java.util.*;
public class Warmup {
public static void versionOfRecursion(int N){
	
		System.out.println("There is a version of recursion.");
		N--;
		if(N>0){
			versionOfRecursion(N);
		}
	}


	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		   System.out.println("Enter number of times to repeat:");

		   int N = input.nextInt();
		   versionOfRecursion(N);
		   input.close();
	}

}
