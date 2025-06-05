#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;


int main()
{
    int n;
    cin >> n; cin.ignore();
    for (int i = 0; i < n; i++) {
        string card;
        getline(cin, card);

        // Get card number,remove spaces and convert to integer array.
        int arr[16];
        int idx = 0;
        for (int j=0;j<card.length();j++){
            if (card[j] != ' '){
                arr[idx] = (int)(card[j]) - 48;  
                idx+=1; 
            }
        }
        
        // Step 1 and 2
        int sum_val = 0;
        for (int j = 0; j < 16;j+=2){
            if (j%2 == 0){
                if (arr[j] * 2 < 10){
                    sum_val += arr[j] * 2;
                }else{
                    sum_val += arr[j] * 2 - 9;
                }
            }
        }

        // Step 3 - Add odd place values.
        int odd_value = 0;
        for (int j = 1; j < 16;j+=2){
            odd_value += arr[j];
        }

        // Step 4 - Output YES if card is valid otherwise NO.
        if ((odd_value + sum_val) % 10 == 0){
            cout << "YES" << endl;
        }else{
            cout << "NO" << endl;
        }
    }
}
