import java.util.*;
class Solution {

    public static void main(String args[]) {
        // Create hashmap for storing numbers.
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        HashMap<String,Integer> numbs = new HashMap<>(); 

        // For each numbers, add every substring starting from the first position to the hashmap. 
        for (int i = 0; i < N; i++) {
            String telephone = in.next();
            for (int j = 0; j<telephone.length();j++){
                if (!numbs.containsKey(telephone.substring(0, j+1))){
                    numbs.put(telephone.substring(0, j+1),1);
                }
            }
        }
        // The number of elements (referencing a number) stored in the structure.
        System.out.println(numbs.size());
        in.close();
    }
}
