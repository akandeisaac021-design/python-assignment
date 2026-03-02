import java.util.Scanner;

public class PrimeNumberIdentifier{
public static void main(String [] args){

Scanner scanner =new Scanner (System.in);

System.out.println("Enter a number: ");
int number =scanner.nextInt();

int divisor =2;
int count =0;

while (count <=number){
    if (number % count ==0){
        count++;        
    }

} 
if (count >1){
    System.out.println(number + "is not a prime number");
}
else{
    System.out.println(number + "is not a prime number");
}







}
 } 
