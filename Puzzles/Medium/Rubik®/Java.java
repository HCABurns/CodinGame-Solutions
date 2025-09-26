import java.util.*;
class Solution {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        if (n == 1){
            System.out.println(1);
        }else{
            System.out.println((6*(n-2)*(n-2) + 12 * (n-2) + 8));
        }
        in.close();
    }
}
