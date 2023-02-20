/**
 * This program will allow the user to enter a year and give a random boolean guess if it is a leap year and
 * then the true guess
 * CSE 174
 * Section: C
 * @author: Rachel Curci
 */

// Importing the class Scanner
import java.util.Scanner;
// Importing the class Random
import java.util.Random;

public class leapYearChecker
{
    public static void main(String[] args)
    {
        // Creating an object called "user" of class Scanner and passing the "System.in" as the input stream
        Scanner user = new Scanner(System.in);
        System.out.print("Enter a year to test: ");
        // user input assigned to variable called "year"
        int year = user.nextInt();

        // Creating an object called "rand" of class Random
        Random rand = new Random();

        // variable called programGuess for the random true or false guess
        boolean programGuess = rand.nextBoolean();

        System.out.println("You: Is it true/false that " + year + "is a leap year? Initially, the program guessed: " + programGuess);

        // variable called trueGuess for the actual true or false
        boolean trueGuess;
        trueGuess = (year % 400 == 0) || ((year % 4 == 0)  && (year % 100 != 0));

        System.out.println("You: Is it true/false that " + year + " is a leap year? Later, the program found out: " + trueGuess);


    }
}
