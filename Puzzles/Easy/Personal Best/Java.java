import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        // Create hashmaps to be used.
        String[] gymnasts = in.nextLine().split(",");
        String[] cats = {"bars", "beam", "floor"};
        String[] inputCategories = in.nextLine().split(",");
        List<Integer> categories = new ArrayList<>();
        HashMap<String, double[]> athletes = new HashMap<>();
        for (String category : inputCategories) {
            for (int i = 0; i < cats.length; i++) {
                if (cats[i].equals(category)) {
                    categories.add(i);
                    break;
                }
            }
        }    

        // Get the number of scores
        int n = Integer.parseInt(in.nextLine());
        for (int i = 0; i < n; i++) {
            String[] data = in.nextLine().split(",");
            String name = data[0];
            double bars = Double.parseDouble(data[1]);
            double beam = Double.parseDouble(data[2]);
            double floor = Double.parseDouble(data[3]);

            // If athlete already has scores, compare and keep max values
            if (!athletes.containsKey(name)) {
                athletes.put(name, new double[]{bars, beam, floor});
            } else {
                double[] scores = athletes.get(name);
                scores[0] = Math.max(scores[0], bars);
                scores[1] = Math.max(scores[1], beam);
                scores[2] = Math.max(scores[2], floor);
                athletes.put(name, scores);
            }
        }

        // Output scores for each gymnast in the specified categories
        for (String name : gymnasts) {
            if (athletes.containsKey(name)) {
                double[] scores = athletes.get(name);
                List<String> output = new ArrayList<>();
                for (int idx : categories) {
                    double score = scores[idx];
                    if (score == (int) score) {
                        output.add(String.valueOf((int) score));
                    }else{
                        output.add(String.valueOf(score));
                    }
                }
                System.out.println(String.join(",", output));
            }
        }
        in.close();
    }
}
