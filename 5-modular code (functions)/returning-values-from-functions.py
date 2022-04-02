# this is the fourth lesson in chapter 5
# this lesson about returning values from functions

# in python, when creating a function using the def statement, you can to specify what the return value should
# be with a return statement

def withdrow_money(current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
    return current_balance

balance = withdrow_money(100, 20)

if (balance <= 50):
    print("the balance is: ", balance, " and we need to make a deposit!")
else:
    print("nothing to see here!")