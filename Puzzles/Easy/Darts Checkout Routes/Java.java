import java.util.*;

public class Solution {
    static Map<Integer, String> singles = new HashMap<>();
    static Map<Integer, String> doubles = new HashMap<>();
    static Map<Integer, String> trebles = new HashMap<>();
    static Set<List<String>> combinations = new HashSet<>();

    public static void main(String[] args) {
        // Get inputs.
        Scanner scanner = new Scanner(System.in);
        int score = scanner.nextInt();
        int darts = scanner.nextInt();
        scanner.close();

        // Populate singles, doubles and trebles.
        for (int i = 1; i <= 20; i++) {
            singles.put(i, String.valueOf(i));
            doubles.put(i * 2, "D" + i);
            trebles.put(i * 3, "T" + i);
        }
        singles.put(25, "25");
        doubles.put(50, "D25");

        // Perfrom DFS to find number of combinations and print that value.
        search(score, new ArrayList<>(), darts);
        System.out.println(combinations.size());
    }

    public static void search(int score, List<String> darts, int left) {
        if (score < 0 || left == -1) {
            return;
        }

        if (score == 0 && !darts.isEmpty() && darts.get(darts.size() - 1).startsWith("D")) {
            combinations.add(new ArrayList<>(darts));
            return;
        }

        // Select all darts or only double if 1 dart remaining.
        List<Map<Integer, String>> dartTypes = left > 1 
            ? Arrays.asList(singles, doubles, trebles) 
            : Arrays.asList(doubles);

        // Search each of the combinations.
        for (Map<Integer, String> arr : dartTypes) {
            for (Map.Entry<Integer, String> entry : arr.entrySet()) {
                List<String> newDarts = new ArrayList<>(darts);
                newDarts.add(entry.getValue());
                search(score - entry.getKey(), newDarts, left - 1);
            }
        }
    }
}
