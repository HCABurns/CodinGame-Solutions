import std;
import std.math;
import std.math.constants : PI;

void main()
{
    auto inputs = readln.split;
    float side = inputs[0].to!float;
    float diameter = inputs[1].to!float;

    // Calculate wasteful bakers amount.
    int wasteful = (pow(floor(side / diameter),2)).to!int;

    // Calculate frugal bakers amount.
    float frugal = 0;
    float area = side*side;
    while (side > diameter){
        // Calculate amount possible to be cut.
        float amount = floor(side / diameter);
        amount *= amount;
        // Convert wasted into a new dough rectangle.
        frugal += amount;
        area -= amount * (PI*pow((diameter/2),2));
        side = sqrt(area);
    }

    // Output the correct number.
    writeln((frugal - wasteful));
}
