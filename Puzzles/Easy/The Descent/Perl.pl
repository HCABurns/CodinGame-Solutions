use strict;
use warnings;
use 5.32.1;
select(STDOUT); $| = 1; # DO NOT REMOVE

# game loop
while (1) {
    # Declare required variables.
    my $max_v = 0;
    my $max_i = 0;

    # Find the index of the max height and store in max_index.
    for my $i (0..7) {
        chomp(my $mountain_h = <STDIN>); 
        if($mountain_h > $max_v){
            $max_v = $mountain_h;
            $max_i = $i;
        }
    }
    
    # Output the index of the mountain to fire on.
    print "$max_i\n"; 
}
