import std;

void main()
{
    // Define variables.
    int N = readln.chomp.to!int;
    int[] arr;

    // Fill array with horse strength.
    for (int i = 0; i < N; i++) {
        int pi = readln.chomp.to!int;
        arr ~= pi;
    }

    // Sort array.
    arr.sort();

    // Define difference.
    int difference = 9999999;

    // Check adjacent horses power and store minimum difference.
    for (int i = 0; i < N-1; i++) {
        int val = arr[i+1] - arr[i];
        if (val < difference){
            difference = val;
        }
    }
    // Output the min difference
    writeln(difference);
}
