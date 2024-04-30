#ifndef ACCOUNT_HPP
# define ACCOUNT_HPP

# include <iostream>
# include "Bank.hpp"

class Bank;

class Account {
private:
    int id;
    int value;
    friend class Bank; // Allow Bank class to access private members

    Account(int _id, int _value) : id(_id), value(_value);

public:
    int getId() const;
    int getValue() const;
};

#endif
