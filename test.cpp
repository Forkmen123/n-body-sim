#include <iostream>
#include <string>
using namespace std;


void changeValue(int &num) {
    num = 50;
}

int main() {
    int value = 10;
    changeValue(value);
    cout << value;
    
    return 0;
}