#include <iostream>
using namespace std;

int main() {
    int choice;
    double balance = 10000; // starting balance
    double amount;

    while (true) { // infinite loop until user chooses to exit
        // Display menu
        cout << "\n===== ATM MENU =====" << endl;
        cout << "1. Check Balance" << endl;
        cout << "2. Deposit" << endl;
        cout << "3. Withdraw" << endl;
        cout << "4. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        // Use nested if-else for options
        if (choice == 1) {
            cout << "Your current balance is: " << balance << endl;
        }
        else if (choice == 2) {
            cout << "Enter amount to deposit: ";
            cin >> amount;
            if (amount > 0) {
                balance += amount;
                cout << "Deposit successful! New balance = " << balance << endl;
            } else {
                cout << "Invalid amount." << endl;
            }
        }
        else if (choice == 3) {
            cout << "Enter amount to withdraw: ";
            cin >> amount;
            if (amount <= 0) {
                cout << "Invalid amount." << endl;
            } else if (amount > balance) {
                cout << "Insufficient balance." << endl;
            } else {
                balance -= amount;
                cout << "Withdrawal successful! Remaining balance = " << balance << endl;
            }
        }
        else if (choice == 4) {
            cout << "Thank you for using the ATM. Goodbye!" << endl;
            break; // exit the loop
        }
        else {
            cout << "Invalid option. Please try again." << endl;
        }
    }

    return 0;
}
