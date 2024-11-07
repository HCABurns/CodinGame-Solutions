import java.util.*;

class Solution {

    public static void main(String args[]) {
        // Get inputs.
        Scanner in = new Scanner(System.in);
        int rows = in.nextInt();
        if (in.hasNextLine()) {
            in.nextLine();
        }

        // Form hashmap of characters and coordinates.
        HashMap<Character,String> chars = new HashMap<>();
        for (int i = 0; i < rows; i++) {
            String[] row = in.nextLine().split(" ");
            for(int j = 0; j < row.length;j++){
                chars.put(row[j].charAt(0), (String.valueOf(i)+String.valueOf(j)));
            }
        }

        // Convert the text to coordinates.
        StringBuilder sb = new StringBuilder();
        String message = in.nextLine();
        for (int i =0; i < message.length();i++){
            sb.append(chars.get(message.charAt(i)));
        }

        // Output the converted text.
        System.out.println(sb.toString());
        in.close();
    }
}
