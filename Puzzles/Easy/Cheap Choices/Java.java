import java.util.*;

class Solution {

    public static void main(String args[]) {
        // Declare required variables.
        Scanner in = new Scanner(System.in);
        int c = in.nextInt();
        int p = in.nextInt();
        HashMap<String,ArrayList<Integer>> items = new HashMap<>();
        if (in.hasNextLine()) {
            in.nextLine();
        }

        // Create Hashmap with item name : array of item costs.
        for (int i = 0; i < c; i++) {
            String item = in.nextLine();
            String[] split = item.split(" ");
            
            StringBuilder string_builder = new StringBuilder();
            for (int j =0; j<split.length-1;j++){
                string_builder.append(split[j]);
                string_builder.append(" ");
            }
            String name = string_builder.toString();
            if (items.containsKey(name) == true){
                items.get(name).add(Integer.parseInt(split[split.length-1]));
            }
            else{
                ArrayList<Integer> arr = new ArrayList<>();
                arr.add(Integer.parseInt(split[split.length-1]));
                items.put(string_builder.toString() , arr);
            }
        }

        // Check each customer request find minimum cost for requested item.
        for (int i = 0; i < p; i++) {
            String order = in.nextLine()+" ";
            int min_cost = -1;
            
            if (items.containsKey(order) == true){
                ArrayList<Integer> costs = items.get(order);
                int min_i = 0;
                for (int j = 0; j<costs.size();j++){
                    if (min_cost == -1 || costs.get(j) < min_cost && costs.get(j) != -1){
                        min_i = j;
                        min_cost = costs.get(j);
                    }
                }
                costs.set(min_i, -1);
            }

            // Output the cost if available otherwise NONE.
            if (min_cost != -1){
                System.out.println(min_cost);
                
            }else{
                System.out.println("NONE");
            }
            

        }
    }
}
