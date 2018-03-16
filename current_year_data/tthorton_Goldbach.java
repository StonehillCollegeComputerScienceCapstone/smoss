import java.util.*;
public class Goldbach {

	
	
	public static void goldbach(int n){
		for(int i = 3; i < n; i++)
			if (isPrime(i) && isPrime(n - i)) {
				System.out.println(n + " = " + (n-i) + " + " + i);
				break;
			}
		}
	
	public static boolean isPrime(int n){
		if(n<2)
			return false;
		if(n==2)
			return true;
		if(n%2==0)
			return false;
		for(int x = 3; x*x<=n; x+=2)
		if(n%x==0)
			return false;
		return true;
	}
	
	public static void main(String[] args) {
		int x = 1;
		Scanner k = new Scanner(System.in);
		while(x ==1)
		{
			System.out.println("Enter a positive integer greater than 2: ");
			int n = k.nextInt();
			goldbach(n);
			System.out.println("Again? 1 for yes: ");
			x = k.nextInt();
		}
		k.close();
	}
}
