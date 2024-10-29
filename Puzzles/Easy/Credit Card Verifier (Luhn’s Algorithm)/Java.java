import java.util.*;

class Solution {

    public static void main(String args[]) {
        // Get number of cards to check.
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        if (in.hasNextLine()) {
            in.nextLine();
        }

        // Get card number,remove spaces and convert to integer array.
        for (int i = 0; i < n; i++) {
            int[] arr = new int[16];
            String card = in.nextLine();
            int idx = 0;
            for (int j=0;j<card.length();j++){
                if (card.charAt(j) != ' '){
                    arr[idx] = (Character.getNumericValue(card.charAt(j)));  
                    idx+=1; 
                }
            }

            // Step 1 and 2
            int sum_val = 0;
            for (int j = 0; j < arr.length;j+=2){
                if (j%2 == 0){
                    if (arr[j] * 2 < 10){
                        sum_val += arr[j] * 2;
                    }else{
                        sum_val += arr[j] * 2 - 9;
                    }
                }
            }

            // Step 3 - Add odd place values.
            int odd_value = 0;
            for (int j = 1; j < arr.length;j+=2){
                odd_value += arr[j];
            }

            // Step 4 - Output YES if card is valid otherwise NO.
            if ((odd_value + sum_val) % 10 == 0){
                System.out.println("YES");
            }else{
                System.out.println("NO");
            }
        }
        in.close();
    }
}
