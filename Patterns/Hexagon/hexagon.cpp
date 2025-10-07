#include <iostream>
using namespace std;

int main() {
    int n = 4;       
    int width = 13;  
    for (int i = 0; i < n; i++) {
        int stars = width/2 + i*2;
        int spaces = (width - stars)/2;
        for (int s = 0; s < spaces; s++) cout << " ";
        for (int s = 0; s < stars; s++) cout << "*";
        cout << endl;
    }


    for (int i = n-2; i >= 0; i--) {
        int stars = width/2 + i*2;
        int spaces = (width - stars)/2;
        for (int s = 0; s < spaces; s++) cout << " ";
        for (int s = 0; s < stars; s++) cout << "*";
        cout << endl;
    }

    return 0;
}
