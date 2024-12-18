import java.util.*;
class Solution {
    public static void main(String args[]) {
        // Get rounds amount and starting cash amount.
        Scanner in = new Scanner(System.in);
        int rounds = in.nextInt();
        int cash = in.nextInt();
        if (in.hasNextLine()) {
            in.nextLine();
        }
        
        for (int i = 0; i < rounds; i++) {
            // Get bet and remove from cash.
            int bet_amount = Math.ceilDiv(cash,4);
            cash -= bet_amount;

            // Get the play and get required variables.
            String[] play = in.nextLine().split(" ");
            int number = Integer.valueOf(play[0]);
            String bet = play[1];

            // Detemrine if bet it a win or loss. 
            if (bet.equals("ODD")){
                if (number % 2 == 1){
                    cash += bet_amount * 2;
                }
            }else if (bet.equals("EVEN")){
                if (number != 0 && number % 2 == 0){
                    cash += bet_amount * 2;
                }
            }else{
                if (number == Integer.valueOf(play[2])){
                    cash += bet_amount * 36;
                }
            }
        }
        // Print cash after playing.
        System.out.println(cash);
        in.close();
    }
}
