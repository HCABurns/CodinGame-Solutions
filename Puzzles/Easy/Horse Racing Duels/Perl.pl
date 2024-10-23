select(STDOUT); $| = 1; # DO NOT REMOVE

# Get size of inputs and store in a array.
chomp(my $n = <STDIN>);
my @f = [];
for my $i (0..$n-1) {
    chomp(my $pi = <STDIN>);
    push @f, $pi;
}

# Sort array.
@f=sort { $a <=> $b } @f;

# Define difference variable
my $difference = 10000001;

# Check adjacent horses power and store minimum difference.
for my $i (0..$n-1){
    if (($f[$i+1]-$f[$i])<$difference){
        $difference = $f[$i+1]-$f[$i];
    }
}
# Output minimum difference
print $difference;
