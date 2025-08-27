#include <iostream>
using namespace std;

int main() {
    int choice;
    double a, b;

    while (true) {
        // Menu
        cout << "\n?? Simple Calculator\n";
        cout << "1. Addition\n";
        cout << "2. Subtraction\n";
        cout << "3. Multiplication\n";
        cout << "4. Division\n";
        cout << "5. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        // Exit condition
        if (choice == 5) {
            cout << "Exiting... Bye!\n";
            break;
        }

        // Taking numbers
        cout << "Enter first number: ";
        cin >> a;
        cout << "Enter second number: ";
        cin >> b;

        // Switch for operations
        switch (choice) {
            case 1:
                cout << "Result = " << (a + b) << endl;
                break;
            case 2:
                cout << "Result = " << (a - b) << endl;
                break;
            case 3:
                cout << "Result = " << (a * b) << endl;
                break;
            case 4:
                if (b != 0)
                    cout << "Result = " << (a / b) << endl;
                else
                    cout << "Error: Division by zero!" << endl;
                break;
            default:
                cout << "Invalid choice! Please try again." << endl;
        }
    }

    return 0;
}

