// Get size of Triforce.
const N = parseInt(readline());

// Print top half 
for (let i = 1;i<N+1;i++){
    if (i == 1){
        console.log("." + " ".repeat(2*N-i-1) + "*".repeat(2*i-1))
    }
    else{
        console.log(" ".repeat(2*N-i) + "*".repeat(2*i-1))
    }
}

// Print bottom half
for (let i = 1;i<N+1;i++){
    left = " ".repeat(N-i) + "*".repeat(2*i-1)
    right = "*".repeat(2*i-1)
    console.log(left + " ".repeat(2*(N-i)+1) + right)
}
