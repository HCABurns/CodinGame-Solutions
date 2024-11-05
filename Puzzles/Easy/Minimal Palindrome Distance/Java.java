import java.util.*;
class Solution {

    public static void main(String args[]) {
        // Get input string and size.
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        if (in.hasNextLine()) {
            in.nextLine();
        }
        String s = in.nextLine();

        // Find Longest palindrome starting from the back.
        int longest = 1;
        for (int j = 0; j < n;j++){
            String subString = s.substring(n-j-1, n);
            if (subString.equals(new StringBuilder(subString).reverse().toString()) && j > longest){
                longest = j + 1;
            }
        }

        // Print number of chars that need to be added from the front to make a palindrome.
        System.out.println(n - longest);
        in.close();
    }
}
