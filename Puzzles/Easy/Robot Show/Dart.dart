import 'dart:io';
import 'dart:math';

String readLineSync() {
  String? s = stdin.readLineSync();
  return s == null ? '' : s;
}

void main() {
  // Get inputs.
    List inputs;
    int L = int.parse(readLineSync());
    int N = int.parse(readLineSync());
    inputs = readLineSync().split(' ');

    // Form array of bots positions.
    var arr = [];
    for (int i = 0; i < N; i++) {
        int b = int.parse(inputs[i]);
        arr.add(b);
    }

    // Max time is for a furthest box from the end to reach the end.
    int max_val = arr.reduce((curr, next) => curr > next? curr: next);
    int min_val = arr.reduce((curr, next) => curr < next? curr: next);
    print(max(L-min_val,max_val));
}
