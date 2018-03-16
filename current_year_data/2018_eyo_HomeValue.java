import java.util.Scanner;
public class HomeValue{
public static void main (String[] args){
double i=300000;
double x,y,r,u,e,d;
Scanner keyboard = new Scanner(System.in);
System.out.println("please enter number of years of investment:");
int b= keyboard.nextInt();
switch(b){
case 1:
System.out.println("please enter the value(s) of change:");
x= keyboard.nextDouble();
System.out.println(i*(1+(x/100)));

break;
case 2:
System.out.println("please enter the value(s) of change:");
x=keyboard.nextDouble();
y=keyboard.nextDouble();
geometricMean(i,x,y);
System.out.println(geometricMean(i,x,y));
break;
case 3:
System.out.println("please enter the value(s) of change:");
x=keyboard.nextDouble();
y=keyboard.nextDouble();
r=keyboard.nextDouble();
geometricMean(i,x,y,r);
System.out.println(geometricMean(i,x,y,r));
break;
case 4:
System.out.println("please enter the value(s) of change:");
x=keyboard.nextDouble();
y=keyboard.nextDouble();
r=keyboard.nextDouble();
u=keyboard.nextDouble();
geometricMean(i,x,y,r,u);
System.out.println(geometricMean(i,x,y,r,u));
break;
case 5:
System.out.println("please enter the value(s) of change:");
x=keyboard.nextDouble();
y=keyboard.nextDouble();
r=keyboard.nextDouble();
u=keyboard.nextDouble();
e=keyboard.nextDouble();
geometricMean(i,x,y,r,u,e);
System.out.println(geometricMean(i,x,y,r,u,e));
break;
case 6:
System.out.println("please enter the value(s) of change:");
x=keyboard.nextDouble();
y=keyboard.nextDouble();
r=keyboard.nextDouble();
u=keyboard.nextDouble();
e=keyboard.nextDouble();
d=keyboard.nextDouble();
geometricMean(i,x,y,r,u,e,d);
System.out.println(geometricMean(i,x,y,r,u,e,d));
break;
default:
System.out.println("please enter number of years of investment:");
}

}
public static double geometricMean(double i,double x,double y){
return(i*((1+(x/100))+(1+(y/100))));

}
public static double geometricMean(double i,double x,double y,double r){
return (i*((1+(x/100))+(1+(y))+(1+(r/100))));

}
public static double geometricMean(double i,double x,double y,double r,double u){

return(i*((1+(x/100))+(1+(y/100))+(1+(r/100))+(1+(u/100))));
}
public static double geometricMean(double i,double x,double y,double r,double u,double e){

return(i*((1+(x/100))+(1+(y/100))+(1+(r/100))+(1+(u/100))+(1+(e/100))));
}
public static double geometricMean(double i,double x,double y,double r,double u,double e,double d){

return(i*((1+(x/100))+(1+(y/100))+(1+(r/100))+(1+(u/100))+(1+(e/100))+(1+(d/100))));
}






}