import java.util.*;
import java.lang.StringBuilder;

class Solution {

    public static void main(String args[]) {
        
        // Create map to convert char to int and visa verse
        HashMap<Integer,String> map = new HashMap<Integer,String>();
        map.put(0, "_");
        map.put(1, "-");
        HashMap<String,Integer> reverse_map = new HashMap<String,Integer>();
        reverse_map.put("_", 0);
        reverse_map.put("-", 1);
        // Create map to keep name assigned with input string.
        HashMap<String,String> map2 = new HashMap<String,String>();

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        // Asign name and signal to the hashmap.
        for (int i = 0; i < n; i++) {
            String inputName = in.next();
            String inputSignal = in.next();
            map2.put(inputName , inputSignal);
        }

        // Go through each output required and perfrom the operation.
        for (int i = 0; i < m; i++) {
            String outputName = in.next();
            String type = in.next();
            String inputName1 = in.next();
            String inputName2 = in.next();

            // Get correct strings
            String v1 = map2.get(inputName1);
            String v2 = map2.get(inputName2);
            
            // StringBuilder object to from an output.
            StringBuilder s = new StringBuilder();

            // Go through each character and perfrom correct operation and 
            for (int j =0;j<v1.length();j++){
                int char1 = reverse_map.get(String.valueOf(v1.charAt(j)));
                int char2 = reverse_map.get(String.valueOf(v2.charAt(j)));

                int val = 0;
                switch(type){
                    case "AND":
                        s.append(map.get(char1&char2));
                        break;
                    case "OR":
                        s.append(map.get(char1|char2));
                        break;
                    case "XOR":
                        s.append(map.get(char1^char2));
                        break;
                    case "NAND":
                        val = char1&char2;
                        if (val==0){val=1;}
                        else{val=0;}
                        s.append(map.get(val));
                        break;
                    case "NOR":
                        val = char1|char2;
                        if (val==0){val=1;}
                        else{val=0;}
                        s.append(map.get(val));
                        break;
                    default:
                        val = char1^char2;
                        if (val==0){val=1;}
                        else{val=0;}
                        s.append(map.get(val));
                }
            }
            // Output name and string after operation has been performed
            System.out.println(outputName +" " + s.toString());
        }
    }
}
