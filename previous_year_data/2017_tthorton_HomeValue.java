import java.util.*;
public class HomeValue {

	public static double geometricMean2(double one, double two){
		return Math.pow(one*two,.5);
	}
	public static double geometricMean3(double one, double two, double three){
		return Math.pow(one*two*three,.33);
	}
	public static double geometricMean4(double one, double two, double three, double four){
		return Math.pow(one*two*three*four,.25);
	}
	public static double geometricMean5(double one, double two, double three, double four, double five){
		return Math.pow(one*two*three*four*five,.20);
	}
	public static double geometricMean6(double one, double two, double three, double four, double five, double six){
		return Math.pow(one*two*three*four*five*six,.16);
	}
	
	public static void main(String[] args) {
		Scanner k = new Scanner(System.in);
		int x = 1;
		while(x == 1)
		{
		double one=0,two=0,three=0,four=0,five=0,six=0,temp=0;
		
		System.out.println("Please state to the initial investment of your home: ");
		double start = k.nextDouble();
		System.out.println("Please enter the length of your investment (1-6 years): ");
		int years = k.nextInt();
		
		System.out.println("Please enter the following values increase/decrease in the format (1.00 = 0% change, -0.93 = 7% decrease, 1.20 = 20% increase.).");
		
		System.out.println("Please enter the first year change: ");
		one = k.nextDouble();
		
		if(years>1){
		System.out.println("Please enter the second year change: ");
		two = k.nextDouble();}
		
		if(years>2){
		System.out.println("Please enter the third year change: ");
		three = k.nextDouble();}
		
		if(years>3){
		System.out.println("Please enter the fourth year change: ");
		four = k.nextDouble();}
		
		if(years>4){
		System.out.println("Please enter the fifth year change: ");
		five = k.nextDouble();}
		
		if(years>5){
		System.out.println("Please enter the sixth year change: ");
		six = k.nextDouble();}
		
		if(years==1){
			System.out.println("Your home value is now: " + start*one);
			System.out.println("Run again? Type '1' to continue: ");
			x = k.nextInt();}
		
		if(years==2){
			temp = geometricMean2(one,two);
			System.out.println("Your home value is now: " + start*temp);
			System.out.println("Run again? Type '1' to continue: ");
			x = k.nextInt();}
		
		if(years==3){
			temp = geometricMean3(one,two,three);
			System.out.println("Your home value is now: " + start*temp);
			System.out.println("Run again? Type '1' to continue: ");
			x = k.nextInt();}
		
		if(years==4){
			temp = geometricMean4(one,two,three,four);
			System.out.println("Your home value is now: " + start*temp);
			System.out.println("Run again? Type '1' to continue: ");
			x = k.nextInt();}
		
		if(years==5){
			temp = geometricMean5(one,two,three,four,five);
			System.out.println("Your home value is now: " + start*temp);
			System.out.println("Run again? Type '1' to continue: ");
			x = k.nextInt();}
		
		if(years==6){
			temp = geometricMean6(one,two,three,four,five,six);
			System.out.println("Your home value is now: " + start*temp);
			System.out.println("Run again? Type '1' to continue: ");
			x = k.nextInt();}
		
		}
		k.close();
	}

}
