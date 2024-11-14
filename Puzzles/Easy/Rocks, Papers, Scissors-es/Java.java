import java.util.*;
class Solution {
    public static void main(String args[]) {
        // Define maps to be used.
        Map<String, String> beats = Map.of("Scissors", "Paper","Paper", "Rock","Rock", "Scissors");
        Map<String, String> loses = Map.of("Scissors", "Rock","Paper", "Scissors","Rock", "Paper");

        // Get all players choices and store in array.
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        if (in.hasNextLine()) {
            in.nextLine();
        }
        String[] players = new String[n];
        for (int i = 0; i < n; i++) {
            String a = in.nextLine();
            players[i] = a;
        }

        // Find the best choice and starting position to win the most without losing once.
        int max_winning = 0;
        ArrayList<Object> max_selection = new ArrayList<>();
        max_selection.add("");
        max_selection.add(0);
        int wins;
        int first_opponent_idx;
        for (int i = 0; i < n ; i++){
            first_opponent_idx = (i+1)%n;
            wins = 0;
            String player_selection = loses.get(players[first_opponent_idx]);
            for (int j = 0; j < n-1;j++){
                if (beats.get(player_selection).equals(players[(first_opponent_idx+j)%n])){
                    wins+=1;
                }else if (loses.get(player_selection).equals(players[(first_opponent_idx+j)%n])){
                    break;
                }
            }
            // Set new max is more wins than previous max.
            if (wins > max_winning){
                max_winning = wins;
                max_selection.set(0, player_selection);
                max_selection.set(1, first_opponent_idx);
            }
        }
        // Output choice and first opponent id.
        System.out.println(max_selection.get(0));
        System.out.println(max_selection.get(1));
        in.close();
    }
}
