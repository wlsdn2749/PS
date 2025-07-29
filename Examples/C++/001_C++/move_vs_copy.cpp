#include <iostream>
#include <vector>

struct Foo {
    std::vector<int> v;
    Foo() = default;

    Foo(const Foo& rhs)      : v(rhs.v) { std::cout << "copy\n"; }
    Foo(Foo&& rhs) noexcept  : v(std::move(rhs.v)) { std::cout << "move\n"; }
};

int main() {
    Foo a;
    a.v.resize(1000, 1);

    Foo b = a;          // copy
    Foo c = std::move(a); // move

    std::cout << "a.v.size = " << a.v.size() << '\n'; // 0
    std::cout << "c.v.size = " << c.v.size() << '\n'; // 1000
}