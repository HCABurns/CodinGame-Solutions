import java.util.*;
class Solution {
    public static void main(String args[]) {
        // Get inputs.
        Scanner in = new Scanner(System.in);
        int A1 = in.nextInt();
        int N = in.nextInt();

        // Create hashmap for storing indexes.
        HashMap<Integer,Integer> hashmap = new HashMap<>();

        // Complete sequence.
        for (int i = 0; i<N-1;i++){
            if (!hashmap.containsKey(A1)){
                hashmap.put(A1, i);
                A1 = 0;
            }else{
                int tmp = (i - hashmap.get(A1));
                hashmap.put(A1, i);
                A1 = tmp;
            }
        }
        // Output the value.
        System.out.println(A1);
        in.close();
    }
}
