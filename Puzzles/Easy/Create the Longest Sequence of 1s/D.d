import std;

void main()
{
    string b = readln.chomp;

    // Split the string on '0's.
    string[] arr = b.split('0');

    // Get max size of two adjacent sets of 1s.
    int max_size = 0;

    for (size_t i = 0; i < arr.length - 1; i++) {
        int size = cast(int)(arr[i].length + arr[i + 1].length);
        if (size > max_size) {
            max_size = size;
        }
    }

    // Print result.
    writeln(max_size + 1);
}
