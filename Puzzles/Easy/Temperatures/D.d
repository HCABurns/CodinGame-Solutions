import std;

void main()
{
    int n = readln.chomp.to!int; // the number of temperatures to analyse
    auto inputs = readln.split;

    // Find temp closest to 0 and prioritise positive over negatives if equal.
    int temp = -999999;
    for (int i = 0; i < n; i++) {
        int t = inputs[i].to!int; // a temperature expressed as an integer ranging from -273 to 5526
        if (abs(t) < abs(temp)){
            temp = t;
        }else if (abs(t) == abs(temp)){
            temp = max(t,temp);
        }
    }

    // Print correct output.
    if (temp != -999999){
        writeln(temp);
    }else{
        writeln("0");
    }
}

