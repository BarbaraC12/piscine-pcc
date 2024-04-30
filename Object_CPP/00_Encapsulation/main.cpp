#include <iostream>
#include "Bank.hpp"

int main() {
    Bank bank;

    bank.createAccount(0, 100);
    bank.createAccount(1, 100);

    std::cout << "Initial Bank State:\n" << bank << "\n";

    bank.deposit(0, 200);
    bank.deposit(1, 300);

    std::cout << "Bank State after deposits:\n" << bank << "\n";

    bank.giveLoan(0, 50);

    std::cout << "Bank State after loan:\n" << bank << "\n";

    return 0;
}
