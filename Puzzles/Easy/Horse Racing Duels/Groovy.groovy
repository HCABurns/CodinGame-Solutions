import java.util.Scanner
import java.util.Arrays

def input = new Scanner(System.in)

// Declare required variables.
int N = input.nextInt()
def int[] arr = new int[N]
def difference = 99999999

// Store horse strength in array.
for (int i = 0; i < N; ++i) {
    arr[i] = input.nextInt()
}

// Sort the array in place
Arrays.sort(arr)

// Check adjacent horses power and store minimum difference.
for (i = 0; i < N-1; ++i) {
    int val = arr[i+1] - arr[i]
    if (val < difference){
        difference = val
    }
}

// Output the min difference
println difference
