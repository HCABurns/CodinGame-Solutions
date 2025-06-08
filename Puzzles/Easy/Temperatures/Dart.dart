import 'dart:io';
import 'dart:math';

String readLineSync() {
  String? s = stdin.readLineSync();
  return s == null ? '' : s;
}

void main() {
    List inputs;
    int n = int.parse(readLineSync()); // the number of temperatures to analyse

    // Find temp closest to 0 and prioritise positive over negatives if equal.
    int temp = 999999;
    inputs = readLineSync().split(' ');
    for (int i = 0; i < n; i++) {
      int t = int.parse(inputs[i]); // a temperature expressed as an integer ranging from -273 to 5526
      if (t.abs() < temp.abs()){
        temp = t;
      }else if (t.abs() == temp.abs()){
        temp = max(t,temp);
      }
    }

    // Print temp closest to zero.
    if (temp != 999999){
      print(temp);
    }else{
      print("0");
    }
}
