#include <iostream>
#include <sstream>
#include <string>
using namespace std;

// Node for our stack
class Node {
public:
    int data;
    Node* next;
    Node(int d) : data(d), next(NULL) {}
};

// Custom Stack implementation
class Stack {
private:
    Node* top;

public:
    Stack() { top = NULL; }

    void push(int val) {
        Node* newNode = new Node(val);
        newNode->next = top;
        top = newNode;
    }

    int pop() {
        if (isEmpty()) {
            cout << "Error: Stack underflow!" << endl;
            return 0;
        }
        int val = top->data;
        Node* temp = top;
        top = top->next;
        delete temp;
        return val;
    }

    bool isEmpty() {
        return top == NULL;
    }

    void printStack() {
        if (isEmpty()) {
            cout << "[Empty Stack]" << endl;
            return;
        }
        Node* temp = top;
        cout << "Stack (top -> bottom): ";
        while (temp != NULL) {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << endl;
    }

    void printTop() {
        if (isEmpty()) cout << "Stack empty!" << endl;
        else cout << top->data << endl;
    }
};

// Evaluate postfix expressions interactively
int main() {
    Stack st;
    string input;

    cout << "Enter tokens (operands/operators). Type ! to exit." << endl;

    while (true) {
        cout << "> ";
        cin >> input;

        // If user enters !
        if (input == "!") {
            cout << "Exiting program..." << endl;
            break;
        }

        // Print stack state
        else if (input == "?") {
            st.printStack();
        }

        // Print top element
        else if (input == "^") {
            st.printTop();
        }

        // Operator handling
        else if (input == "+" || input == "-" || input == "*" || input == "/" || input == "%") {
            if (st.isEmpty()) { cout << "Not enough operands!" << endl; continue; }
            int b = st.pop();
            if (st.isEmpty()) { cout << "Not enough operands!" << endl; continue; }
            int a = st.pop();

            int result = 0;
            if (input == "+") result = a + b;
            else if (input == "-") result = a - b;
            else if (input == "*") result = a * b;
            else if (input == "/") result = b == 0 ? 0 : a / b;
            else if (input == "%") result = a % b;

            st.push(result);
        }

        // Operand (integer)
        else {
            // convert string to int safely
            stringstream ss(input);
            int val;
            if (ss >> val)
                st.push(val);
            else
                cout << "Invalid input!" << endl;
        }
    }

    return 0;
}
