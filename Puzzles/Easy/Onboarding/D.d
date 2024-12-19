import std;

void main()
{
    while (1) {
        string enemy1 = readln.strip; // name of enemy 1
        int dist1 = readln.strip.to!int; // distance to enemy 1
        string enemy2 = readln.strip; // name of enemy 2
        int dist2 = readln.strip.to!int; // distance to enemy 2

        // Print closer enemy.
        if (dist1 < dist2) {
            writeln(enemy1);
        } else {
            writeln(enemy2);
        }
    }
}
