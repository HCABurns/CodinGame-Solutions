// Get inputs.
var inputs: string[] = readline().split(' ');
var side: number = parseFloat(inputs[0]);
var diameter: number = parseFloat(inputs[1]);

// Calculate wasteful bakers amount.
var wasteful = (Math.floor(side / diameter)**2);


// Calculate frugal bakers amount.
var frugal = 0;
var area = side*side;
while (side > diameter){
    // Calculate amount possible to be cut.
    var amount = Math.floor(side / diameter);
    amount *= amount;
    // Convert wasted into a new dough rectangle.
    frugal += amount;
    area -= amount * (Math.PI*Math.pow((diameter/2),2));
    side = Math.sqrt(area);
}

// Output the correct number.
console.log((frugal - wasteful));
