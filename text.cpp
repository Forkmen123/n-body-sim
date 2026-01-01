using namespace std;
#include <iostream>

struct Number {
    int value;
    
    Number(int v) {
        value = v;
    }

    Number operator+(const Number &other) {
        return Number(value + other.value);
    }
    
    void display() {
        cout << value << endl;
    }


};



int main() {
    Number n1(5), n2(10);
    Number n3 = n1 + n2;
    n3.display();
}