def bankoper(initialBal, deposit, withdraw):
    totalBal = initialBal + deposit
    updateBal = totalBal - withdraw

    return totalBal, updateBal


if __name__ == "__main__":
    initialBal = int(input("Enter amount as initial Balance: "))
    deposit = int(input("Enter amount to deposit: "))
    withdraw = int(input("Enter withdraw amount: "))

    total, updateBal = bankoper(initialBal, deposit, withdraw)

    print("Total Balance:", total)
    print("Updated Balance:", updateBal)