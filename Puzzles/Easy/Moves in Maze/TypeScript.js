// Get values.
var grid = [];
var start = [0,0];
var inputs: string[] = readline().split(' ');
const w: number = parseInt(inputs[0]);
const h: number = parseInt(inputs[1]);
for (let i = 0; i < h; i++) {
    let ROW: string = readline();
    var charArray: string[] = Array.from(ROW);
    grid.push(charArray);
    for (let j = 0; j < ROW.length; j++){
        if (charArray[j] == "S"){
            grid[i][j] = ".";
            start = [i,j];
        }
    }
}

// Perform BFS to fill the maze from the start.
let to_visit = [start];
let val = 0;
while (to_visit.length > 0){

    let tmp = []
    while (to_visit.length > 0){
        let node = to_visit.pop()
        let x = (w+node[1]) % w;
        let y = (h+node[0]) % h;

        if (grid[y][x] == "."){
            if (val < 10){
                grid[y][x] = val;
            }else{
                grid[y][x] = String.fromCharCode(val);
            }
            tmp.push([y+1,x]);
            tmp.push([y-1,x]);
            tmp.push([y,x-1]);
            tmp.push([y,x+1]);
        }
        

    }
    // Update to_visit list and character in the sequence
    to_visit = tmp;
    val+=1;
    if (val == 10)
    {
        val=65;
    }
}

// Print the new grid.
for (let i = 0; i < h; i++){
    console.log(grid[i].join(""))
}
