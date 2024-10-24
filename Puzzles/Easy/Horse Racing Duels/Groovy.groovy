import java.util.Scanner
import java.util.Arrays

def input = new Scanner(System.in)

// Declare required variables.
int N = input.nextInt()
int i = 0;
int val = 0;
def int[] arr = new int[N]
def difference = 99999999

// Store horse strength in array.
for (i; i < N; ++i) {
    arr[i] = input.nextInt()
}

// Sort the array in place
Arrays.sort(arr)

// Check adjacent horses power and store minimum difference.
i=0;
for (i; i < N-1; ++i) {
    val = arr[i+1] - arr[i]
    if (val < difference){
        difference = val
    }
}

// Output the min difference
println difference
