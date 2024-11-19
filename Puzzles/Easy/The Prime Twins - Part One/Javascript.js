// Get starting number.
let n = parseInt(readline())+1;

// Two variables to store primes.
let p1 = -1;
let p2 = -1;

// Continue until two primes that has a difference of 2 have been found.
while (p2 == -1){
    // Find if n is a prime.
    let is_prime = true;
    for(let i = 2; i < Math.sqrt(n)+1;i++){
        if (n % i == 0){
            is_prime = false;
            break;
        }
    }
    // If prime, increment by 2 othewise reset variables and increment by 1. 
    if (is_prime != false){
        if (p1 == -1){
            p1 = n;
            n+=2;
        }
        else{
            p2 = n;
        }
    }
    else{
        p1 = -1;
        p2 = -1;
        n += 1;
    }
}

// Output the two primes with a difference of 2.
console.log(p1 , p2);
