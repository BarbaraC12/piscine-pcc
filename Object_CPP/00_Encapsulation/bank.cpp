#include "Bank.hpp"

class Bank {
    bool isUniqueId(int id) const {
        for (const Account &account : clientAccounts) {
            if (account.getId() == id) {
                return false;
            }
        }
        return true;
    }

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

