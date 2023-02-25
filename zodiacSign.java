/**
 * The following program will prompt the user for the month and day of birth
 *              It will then return the astrological sign for the inputed month and day
 * CSE 174
 * section: C
 * @author: Rachel Curci
 */
import java.util.Scanner;
public class zodiacSign
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        System.out.print("Type the month you were born in: ");
        String month = input.nextLine();

        System.out.print("Type the day you were born on: ");
        int day = input.nextInt();



        // if and if else statements to see what month the user has inputed
        // and within the if or if else about the month are
        // nested if and if else statements to determine the zodiac
        // sign from the day inputed
        if (month.equals("January"))
        {
            if (day <= 19)
                System.out.println("The astrological sign for " + month + "/" + day + " is " + ('\u2651') + " - Capricornus (Goat)");
            else
                System.out.println("The astrological sign for " + month + "/" + day + " is " + ('\u2652') + " - Aquarius (Water Bearer)");
        }
        else if (month.equals("February"))
        {
            if (day <= 18)
                System.out.println("The astrological sign for " + month + "/" + day + " is " + ('\u2652') + " - Aquarius (Water Bearer)");
            else
                System.out.println("The astrological sign for " + month + "/" + day + " is " + ('\u2653') + " - Pisces (Fish)");
        }
        else if (month.equals("March"))
        {
            if (day <= 20)
                System.out.println("The astrological sign for " + month + "/" + day + " is " + ('\u2653') + " - Pisces (Fish)");
            else
                System.out.println("The astrological sign for " + month + "/" + day + " is " + ('\u2648') + " - Aries (Ram)");
        }
        else if (month.equals("April"))
        {
            if (day <= 19)
                System.out.println("The astrological sign for " + month + "/" + day + " is " + ('\u2648') + " - Aries (Ram)");
            else
                System.out.println("The astrological sign for " + month + "/" + day + " is " + ('\u2649') + " - Taurus (Bull)");
        }
        else if (month.equals("May"))
        {
            if (day <= 20)
                System.out.println("The astrological sign for " + month + "/" + day + " is " + ('\u2649') + " - Taurus (Bull)");
            else
                System.out.println("The astrological sign for " + month + "/" + day + " is " + ('\u264A') + " - Gemini (Twins)");
        }
        else if (month.equals("June"))
        {
            if (day <= 21)
                System.out.println("The astrological sign for " + month + "/" + day + " is " + ('\u264A') + " - Gemini (Twins)");
            else
                System.out.println("The astrological sign for " + month + "/" + day + " is " + ('\u264B') + " - Cancer (Crab)");
        }
        else if (month.equals("July"))
        {
            if (day <= 22)
                System.out.println("The astrological sign for " + month + "/" + day + " is " + ('\u264B') + " - Cancer (Crab)");
            else
                System.out.println("The astrological sign for " + month + "/" + day + " is " + ('\u264C') + " - Leo (Lion)");
        }
        else if (month.equals("August"))
        {
            if (day <= 22)
            {
                System.out.println("The astrological sign for " + month + "/" + day + " is " + ('\u264C') + " - Leo (Lion)");
            }
            else
                System.out.println("The astrological sign for " + month + "/" + day + " is " + ('\u264D') + " - Virgo (Virgin)");
        }
        else if (month.equals("September"))
        {
            if (day <= 22)
                System.out.println("The astrological sign for " + month + "/" + day + " is " + ('\u264D') + " - Virgo (Virgin)");
            else
                System.out.println("The astrological sign for " + month + "/" + day + " is " + ('\u264E') + " - Libra (Balance)");
        }
        else if (month.equals("October"))
        {
            if (day <= 23)
                System.out.println("The astrological sign for " + month + "/" + day + " is " + ('\u264E') + " - Libra (Balance)");
            else
                System.out.println("The astrological sign for " + month + "/" + day + " is " + ('\u264F') + " - Scorpius (Scorpion)");
        }
        else if (month.equals("Novemeber"))
        {
            if (day <= 21)
                System.out.println("The astrological sign for " + month + "/" + day + " is " + ('\u264F') + " - Scorpius (Scorpion)");
            else
                System.out.println("The astrological sign for " + month + "/" + day + " is " + ('\u2650') + " - Sagittarius (Archer)");
        }
        else
        {
            if (day <= 21)
                System.out.println("The astrological sign for " + month + "/" + day + " is " + ('\u2650') + " - Sagittarius (Archer)");
            else
                System.out.println("The astrological sign for " + month + "/" + day + " is " + ('\u2651') + " - Capricornus (Goat)");
        }
    }
}