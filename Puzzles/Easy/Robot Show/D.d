import std;
import std.algorithm;

void main()
{   
    // Get inputs.
    int L = readln.chomp.to!int;
    int N = readln.chomp.to!int;
    auto inputs = readln.split;

    // Form array of bots positons.
    int[] arr;
    for (int i = 0; i < N; i++) {
        int b = inputs[i].to!int;
        arr ~= b;
    }

    // Max time is for a furthest box from the end to reach the end.
    int maxVal = arr[0];
    int minVal = arr[0];
    for (int i = 0; i < N; i++) {
        if (arr[i] < minVal){
            minVal = arr[i];
        }
        if (arr[i] > maxVal){
            maxVal = arr[i];
        }
    }
    if (L-minVal > maxVal){
        writeln(L-minVal);
    }else{
        writeln(maxVal);
    }
}
