import Foundation

public struct StderrOutputStream: TextOutputStream {
    public mutating func write(_ string: String) { fputs(string, stderr) }
}
public var errStream = StderrOutputStream()

// game loop
while true {
    // Declare required variables.
    var max_i = 0
    var max_v = 0

    //  Find the index of the max height and store in max_i.
    for i in 0...7 {
        let mountainH = Int(readLine()!)!
        if mountainH > max_v{
            max_v = mountainH
            max_i = i
        }
    }
    // Output the index of the mountain to fire on.
    print(max_i)     
}
