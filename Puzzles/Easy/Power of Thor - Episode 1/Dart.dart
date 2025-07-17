import 'dart:io';
import 'dart:math';

String readLineSync() {
  String? s = stdin.readLineSync();
  return s == null ? '' : s;
}

void main() {
    List inputs;
    inputs = readLineSync().split(' ');
    int light_x = int.parse(inputs[0]); // the X position of the light of power
    int light_y = int.parse(inputs[1]); // the Y position of the light of power
    int thor_x = int.parse(inputs[2]); // Thor's starting X position
    int thor_y = int.parse(inputs[3]); // Thor's starting Y position

    // game loop
    while (true) {
        int remainingTurns = int.parse(readLineSync()); // The remaining amount of turns Thor can move. Do not remove this line.

        var o = ["",""];
        // If thor is below light, move north.
        if (light_y < thor_y){
            o[0]="N";
            thor_y-=1;
        }
        // If thor is above light, move south.
        if (light_y > thor_y){
            o[0]="S";
            thor_y+=1;
        }
        // If thor is right of the light, move west.
        if (light_x < thor_x){
            o[1] = "W";
            thor_x+=1;
        }
        // If thor is left of the light, move east.
        if (light_x > thor_x){
            o[1] = "E";
            thor_x-=1;
        }
        // A single line providing the move to be made: N NE E SE S SW W or NW
        print(o[0]+o[1]);
    }
}
