import 'dart:io';

String readLineSync() {
  String? s = stdin.readLineSync();
  return s == null ? '' : s;
}

void main() {
    List inputs;
    int surfaceN = int.parse(readLineSync()); // the number of points used to draw the surface of Mars.
    for (int i = 0; i < surfaceN; i++) {
        inputs = readLineSync().split(' ');
        int landX = int.parse(inputs[0]); // X coordinate of a surface point. (0 to 6999)
        int landY = int.parse(inputs[1]); // Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    }

    // game loop
    while (true) {
        inputs = readLineSync().split(' ');
        int X = int.parse(inputs[0]);
        int Y = int.parse(inputs[1]);
        int hSpeed = int.parse(inputs[2]); // the horizontal speed (in m/s), can be negative.
        int vSpeed = int.parse(inputs[3]); // the vertical speed (in m/s), can be negative.
        int fuel = int.parse(inputs[4]); // the quantity of remaining fuel in liters.
        int rotate = int.parse(inputs[5]); // the rotation angle in degrees (-90 to 90).
        int power = int.parse(inputs[6]); // the thrust power (0 to 4).

        // If speed larger than landing speed, set power to max.
        if (vSpeed>=-39){
          power = 0;
          print("0 0");
        }
        else{
          power=4;
          print("0 4");
        }
    }
}
