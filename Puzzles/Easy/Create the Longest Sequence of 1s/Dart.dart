import 'dart:io';

String readLineSync() {
  String? s = stdin.readLineSync();
  return s == null ? '' : s;
}

void main() {
    String b = readLineSync();

    // Split the string on '0's.
    List arr = b.split('0');

    // Get max size of two adjacent sets of 1s.
    int max_size = 0;
    for (int i = 0; i < arr.length - 1; i++) {
        int size = (arr[i].length + arr[i + 1].length);
        if (size > max_size) {
            max_size = size;
        }
    }

    // Print result.
    print(max_size+1);
}
