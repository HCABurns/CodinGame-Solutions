import java.util.*;

class Solution {

    public static void main(String args[]) {
        // Get inputs
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();

        // ArrayList for storing horses strength
        ArrayList<Integer> lst = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            lst.add(in.nextInt());
        }
        // Define difference variable
        int diff = 999999999;
        // Sort horses on power.
        Collections.sort(lst);
        // Compare adjacent horses and store min difference between them.
        for (int i = 0;i<lst.size()-1;i++){
            if (lst.get(i+1) -lst.get(i) < diff){
                diff = lst.get(i+1) -lst.get(i);
            } 
        }
        //Output the minimum difference
        System.out.println(diff);
    }
}
