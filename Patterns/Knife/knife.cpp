#include <iostream>
using namespace std;

int main() {
    int n = 7;
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n-i; j++) cout << " ";
        for(int j = 1; j <= i; j++) cout << "*";
        cout << endl;
    }
    for(int i = n-1; i >= 1; i--){
        for(int j = 1; j <= n-i; j++) cout << " ";
        for(int j = 1; j <= i; j++) cout << "*";
        cout << endl;
    }
    int stem_width = n / 2;
    int stem_height = n;
    for(int i = 1; i <= stem_height; i++){
        for(int j = 1; j <= n-1; j++) cout << " ";
        for(int j = 1; j <= stem_width; j++) cout << "*";
        cout << endl;
    }

    return 0;
}
