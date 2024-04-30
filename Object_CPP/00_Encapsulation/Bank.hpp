#ifndef BANK_HPP
# define BANK_HPP

# include <iostream>
# include "Account.hpp"

class Account;

class Bank {
private:
    int liquidity;
    std::vector<Account> clientAccounts;

    bool isUniqueId(int id) const;

public:
    Bank() : liquidity(0);
    void deposit(int accountId, int amount);
    bool createAccount(int id, int initialDeposit);
    bool giveLoan(int accountId, int amount);
    friend std::ostream& operator<<(std::ostream& os, const Bank& bank) ;
};

#endif
