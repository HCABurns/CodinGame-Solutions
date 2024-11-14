import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        // Get words to be changed.
        String[] aWordSpelledOut = in.nextLine().split(" ");

        // Get alphabets.
        String[] year1 = "Authority, Bills, Capture, Destroy, Englishmen, Fractious, Galloping, High, Invariably, Juggling, Knights, Loose, Managing, Never, Owners, Play, Queen, Remarks, Support, The, Unless, Vindictive, When, Xpeditiously, Your, Zigzag".split(", ");
        String[] year2 = "Apples, Butter, Charlie, Duff, Edward, Freddy, George, Harry, Ink, Johnnie, King, London, Monkey, Nuts, Orange, Pudding, Queenie, Robert, Sugar, Tommy, Uncle, Vinegar, Willie, Xerxes, Yellow, Zebra".split(", ");
        String[] year3 = "Amsterdam, Baltimore, Casablanca, Denmark, Edison, Florida, Gallipoli, Havana, Italia, Jerusalem, Kilogramme, Liverpool, Madagascar, New-York, Oslo, Paris, Quebec, Roma, Santiago, Tripoli, Uppsala, Valencia, Washington, Xanthippe, Yokohama, Zurich".split(", ");
        String[] year4 = "Alfa, Bravo, Charlie, Delta, Echo, Foxtrot, Golf, Hotel, India, Juliett, Kilo, Lima, Mike, November, Oscar, Papa, Quebec, Romeo, Sierra, Tango, Uniform, Victor, Whiskey, X-ray, Yankee, Zulu".split(", ");
        List<String[]> alphabets = Arrays.asList(year1, year2, year3, year4);

        // Create hashmap where each word links to the correct word in the next set.
        List<Map<String, String>> hashmaps = new ArrayList<>();
        for (int i = 0; i < alphabets.size(); i++) {
            Map<String, String> map = new HashMap<>();
            String[] currentYear = alphabets.get(i);
            String[] nextYear = alphabets.get((i + 1) % 4);
            for (int j = 0; j < currentYear.length; j++) {
                map.put(currentYear[j], nextYear[j]);
            }
            hashmaps.add(map);
        }

        // Find the index of alphabet.
        int maxIdx = 0;
        int maxCount = 0;
        for (int i = 0; i < hashmaps.size(); i++) {
            int count = 0;
            for (String word : aWordSpelledOut) {
                if (hashmaps.get(i).containsKey(word)) {
                    count+=1;
                }
            }
            if (count > maxCount) {
                maxCount = count;
                maxIdx = i;
            }
        }

        // Shift words.
        List<String> output = new ArrayList<>();
        for (String word : aWordSpelledOut) {
            if (hashmaps.get(maxIdx).containsKey(word)) {
                output.add(hashmaps.get(maxIdx).get(word));
            }
        }

        // Output the shifted words.
        System.out.println(String.join(" ", output));
        in.close();
    }
}
