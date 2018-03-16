import java.util.*;

public class Goldbach {

	public static void main(String[] args) {
		Scanner keyboard= new Scanner(System.in);
      
      int interger = 0;
		System.out.println("Enter a integer: ");
		interger = keyboard.nextInt();
		Goldbach(interger);
	}
	public static void Goldbach(int interger)
	{
		if(interger <= 2)
		{
			System.out.println("Re-run the program and enter an interger greater than or equal to 2");
			return;
		}
		if(interger %2!=0)
		{
			System.out.println("Interger is not divisible by 2. Enter an even number: ");
			return;
		}
		Set<Integer> primeNumbers = new HashSet<Integer>();
    
		for(int i=2;i<interger;i++)
		{
			boolean a = true;
			for(int x = 2; x < i; x++)
			{
				if(i%x==0)
				{
					a=false;
					break;
				}
			}
			if(a)
			primeNumbers.add(i);
		}

		for(int i = interger - 1; (i >= interger / 2); i--)
		{
			if(primeNumbers.contains(i) && primeNumbers.contains(interger - i))
			{
				
					System.out.println( i + " + "+(interger-i) + " = " + (interger));
			}
		}
	}

}//end class 