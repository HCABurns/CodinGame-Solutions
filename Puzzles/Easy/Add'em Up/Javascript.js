// Get inputs, map to int and sort in decreasing order.
const N = parseInt(readline());
var inputs = readline().split(' ');
let cards = []
for (let i = 0; i < N; i++) {
    cards.push(parseInt(inputs[i]));
}
cards.sort(function(a, b){return b - a});

// Set total.
let total = 0;

// While there is still cards to be combined, combine the cheapest cost.
while (cards.length > 1){
    // While there is still cards to be combined, combine the cheapest cost.
    let new_card = cards.pop() + cards.pop()
    total += new_card

    // Set last item to new card.
    cards.push(new_card)

    // Set last item to new card.
    cards = cards.sort(function(a, b){return b - a});
}

// Output the minimum cost.
console.log(total);
