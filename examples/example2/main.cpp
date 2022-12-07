#include <iostream>

int func1_1(){
    return 0;
}

int func1_2(){
    return 0;
}

int func1(int var){
    return var > 5 ? func1_1() : func1_2();
}

int func2(){
    return 0;
}

int main(){
    int var = 0;
    std::cin >> var;
    func1(var);
    func2();
    return 0;
}