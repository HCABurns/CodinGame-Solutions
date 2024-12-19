import 'dart:io';

String readLineSync() {
    String? line = stdin.readLineSync();
    return line ?? "";
}

void main() {
    while (true) {
        String enemy1 = readLineSync(); // name of enemy 1
        int dist1 = int.parse(readLineSync()); // distance to enemy 1
        String enemy2 = readLineSync(); // name of enemy 2
        int dist2 = int.parse(readLineSync()); // distance to enemy 2

        // Print closer enemy.
        if (dist1 < dist2) {
            print(enemy1);
        } else {
            print(enemy2);
        }
    }
}
