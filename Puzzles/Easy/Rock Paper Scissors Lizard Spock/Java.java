import java.util.*;

class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();

        // Create hashmap of which items beat which.
        HashMap<String,String> hashmap = new HashMap<>();
        hashmap.put("C", "PL");
        hashmap.put("R", "LC");
        hashmap.put("P","RS");
        hashmap.put("L","PS");
        hashmap.put("S","RC");

        // Create ArrayList of players.
        ArrayList<ArrayList<Object>> players = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            int NUMPLAYER = in.nextInt();
            String SIGNPLAYER = in.next();
            ArrayList<Object> player = new ArrayList<Object>();
            player.add(NUMPLAYER);
            player.add(SIGNPLAYER);
            player.add(new ArrayList<Integer>());
            players.add(player);
        }

        // Simulation Loop
        while (players.size() > 1){

            int i;
            for (i=0;i<players.size();i+=1){
                // Get players.
                ArrayList<Object> p1 = players.get(i); 
                ArrayList<Object> p2 = players.get(i+1); 
                ArrayList<Object> to_remove;
                // Find which player to remove.
                if (p1.get(1).equals(p2.get(1))){
                    if ((Integer)p1.get(0) > (Integer)p2.get(0)){
                        to_remove = p1;
                    }else{
                        to_remove = p2;
                    }
                }
                else if ( hashmap.get(p1.get(1)).contains((CharSequence)p2.get(1)) ){
                    to_remove = p2;
                }
                else{
                    to_remove = p1;
                }

                // Remove losing player from list and add their id to the winners beat array.
                if (to_remove.equals(p1)){
                    ArrayList<Integer> beat = (ArrayList<Integer>) p2.get(2);
                    beat.add((Integer)p1.get(0));
                    p2.set(2, beat);
                }else{
                    ArrayList<Integer> beat = (ArrayList<Integer>) p1.get(2);
                    beat.add((Integer)p2.get(0));
                    p1.set(2, beat);
                }
                players.remove(to_remove);
            }
        }

        // Output winner and ids of players the winner beat.
        System.out.println(players.get(0).get(0).toString());
        ArrayList<Integer> beat = (ArrayList<Integer>) players.get(0).get(2);
        StringBuilder sb = new StringBuilder();
        for (int val : beat) {
            sb.append(val);
            sb.append(" ");
        }
        System.out.println(sb.toString().strip());
        in.close();
        }
}
