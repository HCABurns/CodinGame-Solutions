import 'dart:io';

String readLineSync() {
  String? s = stdin.readLineSync();
  return s == null ? '' : s;
}

void main() {

    // Define variables
    int i = 0;
    int val = 0;
    int difference = 10000000;
    int N = int.parse(readLineSync());
    var arr = <int>[];

  // Fill array with horse strength.
    for (i; i < N; i++) {
        arr.add(int.parse(readLineSync()));
    }
    // Sort array.
    arr.sort((a, b) => a-b);   

    // Reset the index variable and set val variable.
    i=0;

    // Check adjacent horses power and store minimum difference.
    for (i; i < N-1; i++) {
      val = arr[i+1] - arr[i];
      if (val < difference)
        difference = val;
    }

    // Output the min difference
    print(difference);
    exit(0);
}
