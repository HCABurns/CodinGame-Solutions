import java.util.*;
class Solution {
    public static void main(String args[]) {
        // Get inputs, map to int and sort in decreasing order.
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        ArrayList<Integer> cards = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            int x = in.nextInt();
            cards.add(x);
        }
        Collections.sort(cards, Collections.reverseOrder());

        // Set total.
        int total = 0;

        // While there is still cards to be combined, combine the cheapest cost.
        while (cards.size() > 1){
            // Get new card and increment cost.
            int new_card = cards.removeLast() + cards.get(cards.size()-1);
            total += new_card;

            // Set last item to new card.
            cards.set(cards.size()-1,new_card);

            // Sort again with the new card in the list.
            Collections.sort(cards, Collections.reverseOrder());
        }

        // Output total minimum.
        System.out.println(total);
        in.close();
    }
}
