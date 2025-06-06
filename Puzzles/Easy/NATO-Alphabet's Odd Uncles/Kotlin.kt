import java.util.*
import java.io.*
import java.math.*

fun main(args : Array<String>) {
    val input = Scanner(System.`in`)
    val aWordSpelledOut = input.nextLine().split(" ")

    // Get alphabets.
    var year1 = "Authority, Bills, Capture, Destroy, Englishmen, Fractious, Galloping, High, Invariably, Juggling, Knights, Loose, Managing, Never, Owners, Play, Queen, Remarks, Support, The, Unless, Vindictive, When, Xpeditiously, Your, Zigzag".split(", ")
    var year2 = "Apples, Butter, Charlie, Duff, Edward, Freddy, George, Harry, Ink, Johnnie, King, London, Monkey, Nuts, Orange, Pudding, Queenie, Robert, Sugar, Tommy, Uncle, Vinegar, Willie, Xerxes, Yellow, Zebra".split(", ")
    var year3 = "Amsterdam, Baltimore, Casablanca, Denmark, Edison, Florida, Gallipoli, Havana, Italia, Jerusalem, Kilogramme, Liverpool, Madagascar, New-York, Oslo, Paris, Quebec, Roma, Santiago, Tripoli, Uppsala, Valencia, Washington, Xanthippe, Yokohama, Zurich".split(", ")
    var year4 = "Alfa, Bravo, Charlie, Delta, Echo, Foxtrot, Golf, Hotel, India, Juliett, Kilo, Lima, Mike, November, Oscar, Papa, Quebec, Romeo, Sierra, Tango, Uniform, Victor, Whiskey, X-ray, Yankee, Zulu".split(", ")
    var alphabets = Arrays.asList(year1, year2, year3, year4)

    // Create hashmap where each word links to the correct word in the next set.
    var hashmaps = ArrayList<Map<String, String>>();
    for (i in 0..alphabets.size-1) {
        var map = HashMap<String, String>();
        var currentYear = alphabets.get(i)
        var nextYear = alphabets.get((i + 1) % 4)
        for (j in 0..currentYear.size-1) {
            map.put(currentYear[j], nextYear[j])
        }
        hashmaps.add(map)
    }

    // Find the index of alphabet.
    var maxIdx = 0
    var maxCount = 0
    for (i in 0..hashmaps.size-1) {
        var count = 0
        for (word in aWordSpelledOut) {
            if (hashmaps.get(i).containsKey(word)) {
                count+=1
            }
        }
        if (count > maxCount) {
            maxCount = count
            maxIdx = i
        }
    }

    // Shift words.
    var output = ArrayList<String>()
    for (word in aWordSpelledOut) {
        if (hashmaps.get(maxIdx).containsKey(word)) {
            output.add(hashmaps[maxIdx][word.toString()].toString())
        }
    }
    
    // Output the shifted words.
    println(output.joinTo(StringBuilder()," "))
}
