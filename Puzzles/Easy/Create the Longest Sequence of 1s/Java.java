import java.util.*;

class Solution {

    public static void main(String args[]) {
        // Get input string.
        Scanner in = new Scanner(System.in);
        String b = in.nextLine();

        // Split the array on 1s.
        String[] arr = b.split("0");

        // Get max size of two adjacent sets of 1s.
        int max_size = 0;
        int size;
        for (int i = 0; i<arr.length-1;i++){
            size = arr[i].length() + arr[i+1].length();
            if (size > max_size){
                max_size = arr[i].length() + arr[i+1].length();
            }
        }
        // Return output + 1 for the flip bit.
        System.out.println(max_size + 1);
        in.close();
    }
}
