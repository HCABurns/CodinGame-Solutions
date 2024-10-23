const surfaceN: number = parseInt(readline()); // the number of points used to draw the surface of Mars.
for (let i = 0; i < surfaceN; i++) {
    var inputs: string[] = readline().split(' ');
    const landX: number = parseInt(inputs[0]); // X coordinate of a surface point. (0 to 6999)
    const landY: number = parseInt(inputs[1]); // Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
}

// game loop
while (true) {
    var inputs: string[] = readline().split(' ');
    const X: number = parseInt(inputs[0]);
    const Y: number = parseInt(inputs[1]);
    const hSpeed: number = parseInt(inputs[2]); // the horizontal speed (in m/s), can be negative.
    const vSpeed: number = parseInt(inputs[3]); // the vertical speed (in m/s), can be negative.
    const fuel: number = parseInt(inputs[4]); // the quantity of remaining fuel in liters.
    const rotate: number = parseInt(inputs[5]); // the rotation angle in degrees (-90 to 90).
    const power: number = parseInt(inputs[6]); // the thrust power (0 to 4).

    // If speed larger than landing speed, set power to max.
    var new_power: number = 0;
    if (vSpeed >= -39){
        new_power = 0;
    }else{
        new_power = 4;
    }
    console.log('0',new_power);
}
