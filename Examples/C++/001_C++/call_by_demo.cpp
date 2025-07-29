#include <cassert>
#include <iostream>

void modifyByValue(int x)     { x = 99; }
void modifyByReference(int& x){ x = 99; }

int main() {
    int a = 1, b = 1;
    modifyByValue(a);      // a == 1
    modifyByReference(b);  // b == 99
    assert(a == 1);
    assert(b == 99);
    std::cout << "OK\n";
}
