import java.util.*;
class Solution {
    public static void main(String args[]) {
        // Get size.
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();

        // Print top triangle.
        for (int i = 1; i < N+1;i++){
            if (i == 1){
                System.out.println("." + " ".repeat(2*N-i-1) + "*".repeat(2*i-1));
            }else{
                System.out.println(" ".repeat(2*N-i) + "*".repeat(2*i-1));
            }
        }

        // Print bottom triangles.
        for (int i = 1; i < N+1;i++){
            String left = " ".repeat(N-i) + "*".repeat(2*i-1);
            String right = "*".repeat(2*i-1);
            System.out.println(left + " ".repeat(2*(N-i)+1) + right);
        }
        in.close();
    }
}
