import java.util.Random;
import java.util.Scanner;

public class GroupingSystem{

    public static void main(String []args){

System.out.print("Enter total population: ");
int populationToBeGrouped =scanner.nextInt();

String [] names =new String [populationToBeGrouped];
int [] designatedGroup =new int [populationToBeGrouped];

Scanner scanner =new Scanner(System.in);
Random random =new Random();

int min =1;
int max =23;

int count =0;

while (count <populationToBeGrouped){
    System.out.print("Enter your name: ");
    String name =scanner.nextInt();
    names[count] =name;
    designatedGroup[count] =random.nextInt(4);
    count++;

}


    }
}
