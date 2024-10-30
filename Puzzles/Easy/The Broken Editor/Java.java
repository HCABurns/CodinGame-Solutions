import java.util.*;

class Solution {

    public static void main(String args[]) {
        // Get input string.
        Scanner in = new Scanner(System.in);
        String typedKeys = in.nextLine();

        // Create array.
        ArrayList<Character> arr = new ArrayList<>();

        // Place charaters in the correct position, or remove charater if required.
        int i = 0;
        for (int j = 0; j<typedKeys.length();j++){
            char c = typedKeys.charAt(j);

            // Ensure i is in bounds.
            if (i < 0){
                i = 0;
            }else if (i>arr.size()){
                i = arr.size();
            }

            // Check character and perform correct operation.
            if (c == '<'){
                i -= 1;
            }else if (c == '>'){
                i +=1;
            }else if (c == '-'){
                i -= 1;
                if (i != -1){
                    arr.remove(i);
                }
            }else{
                arr.add(i, c);
                i+=1;
            }
        }

        // Output the new string.
        StringBuilder sb = new StringBuilder(arr.size());
        for(Character c: arr){
            sb.append(c);
        }
        System.out.println(sb.toString());
    }
}
