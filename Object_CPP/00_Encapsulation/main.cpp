#include <iostream>

class Bank; // Forward declaration of Bank class

class Account {
private:
    int id;
    int value;
    friend class Bank; // Allow Bank class to access private members

    Account(int _id, int _value) : id(_id), value(_value) {}

public:
    int getId() const { return id; }
    int getValue() const { return value; }
};

class Bank {
private:
    int liquidity;
    std::vector<Account> clientAccounts;

    bool isUniqueId(int id) const {
        for (const Account &account : clientAccounts) {
            if (account.getId() == id) {
                return false;
            }
        }
        return true;
    }

public:
    Bank() : liquidity(0) {}

    void deposit(int accountId, int amount) {
        for (Account &account : clientAccounts) {
            if (account.getId() == accountId) {
                account.value += amount;
                liquidity += amount * 0.05; // Bank receives 5% of the deposit
                break;
            }
        }
    }

    bool createAccount(int id, int initialDeposit) {
        if (isUniqueId(id)) {
            clientAccounts.emplace_back(id, initialDeposit);
            liquidity += initialDeposit * 0.05; // Bank receives 5% of the initial deposit
            return true;
        }
        return false;
    }

    bool giveLoan(int accountId, int amount) {
        for (Account &account : clientAccounts) {
            if (account.getId() == accountId) {
                if (liquidity >= amount) {
                    account.value += amount;
                    liquidity -= amount;
                    return true;
                }
                return false;
            }
        }
        return false;
    }

    friend std::ostream& operator<<(std::ostream& os, const Bank& bank) {
        os << "Bank Information:\n";
        os << "Liquidity: " << bank.liquidity << "\n";
        os << "Client Accounts:\n";
        for (const Account &account : bank.clientAccounts) {
            os << "[" << account.getId() << "] - [" << account.getValue() << "]\n";
        }
        return os;
    }
};

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
