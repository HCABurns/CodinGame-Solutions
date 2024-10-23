import 'dart:io';

String readLineSync() {
  String? s = stdin.readLineSync();
  return s == null ? '' : s;
}

void main() {
    // game loop
    while (true) {
      // Declare required variables.
      int max_i = 0;
      int max_v = 0;

      // Find the index of the max height and store in max_index.
      for (int i = 0; i < 8; i++) {
          int mountainH = int.parse(readLineSync()); 
          if (mountainH > max_v){
              max_v = mountainH;
              max_i = i;
          }
      }
      // Output the index of the mountain to fire on.
      print(max_i);
    }
}
