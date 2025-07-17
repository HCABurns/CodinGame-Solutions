import 'dart:io';
import 'dart:math' as math;
import 'dart:convert';

String readLineSync() {
  String? s = stdin.readLineSync();
  return s == null ? '' : s;
}

void main() {
    List inputs;
    inputs = readLineSync().split(' ');
    double side = double.parse(inputs[0]);
    double diameter = double.parse(inputs[1]);

    // Calculate wasteful bakers amount.
    int wasteful = math.pow((side / diameter).floor(),2).floor();

    // Calculate frugal bakers amount.
    double frugal = 0;
    double area = side*side;
    while (side > diameter){
        // Calculate amount possible to be cut.
        int amount = (side / diameter).floor();
        amount *= amount;
        // Convert wasted into a new dough rectangle.
        frugal += amount;
        area -= amount * (math.pi*math.pow((diameter/2),2));
        side = math.pow(area,0.5).toDouble();
    }
    // Print the number of biscuits difference.
    print((frugal - wasteful).toInt());
}
