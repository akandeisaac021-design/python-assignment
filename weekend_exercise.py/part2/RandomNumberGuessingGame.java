import java.util.Random;
public class RandomNumberGuessingGame{
    public static void main (String []args){

        Scanner scanner =new Scanner(System.in);
        Random random =new Random();

        int min =1;
        int max =50;

        int randomNumber =random.nextInt(max -min +1) +min;

        System.out.print("Try to Guess the random number from(1-50): ");
        int guessedNumber =scanner.nextInt;

        while (guessedNumber < 1 || guessedNumber >50){
            System.out.println("re-enter a valid number from(1-20)");
            guessedNumber =scanner.nextInt();
        }

        while (randomNumber !=guessedNumber){
            
            System.out.println("You guessed in-correctly!!");
            System.out.print("Try to Guess the random number from(1-50): ");
            int guessedNumber =scanner.nextInt;
        }



    }
}
