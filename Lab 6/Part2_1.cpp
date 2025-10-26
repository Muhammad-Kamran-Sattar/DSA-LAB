#include <iostream>
#include <string>
using namespace std;

// Node for characters in a word
class CharNode {
public:
    char data;
    CharNode* next;
    CharNode(char d) {
        data = d;
        next = NULL;
    }
};

// Stack for characters (to store each word)
class CharStack {
public:
    CharNode* top;
    CharStack() {
        top = NULL;
    }

    void push(char c) {
        CharNode* newNode = new CharNode(c);
        newNode->next = top;
        top = newNode;
    }

    string popWord() {
        string word = "";
        while (top != NULL) {
            word += top->data;
            top = top->next;
        }
        // reverse word since stack reverses order of chars
        for (int i = 0; i < word.size() / 2; i++)
            swap(word[i], word[word.size() - i - 1]);
        return word;
    }

    bool empty() {
        return top == NULL;
    }
};

// Node for words (string type)
class WordNode {
public:
    string word;
    WordNode* next;
    WordNode(string w) {
        word = w;
        next = NULL;
    }
};

// Stack for words (to reverse sentence)
class WordStack {
public:
    WordNode* top;
    WordStack() {
        top = NULL;
    }

    void push(string w) {
        WordNode* newNode = new WordNode(w);
        newNode->next = top;
        top = newNode;
    }

    string pop() {
        if (top == NULL) return "";
        string w = top->word;
        top = top->next;
        return w;
    }

    bool empty() {
        return top == NULL;
    }
};

// Function to reverse words using custom stacks
void reverseSentence(string sentence) {
    WordStack sentenceStack;
    CharStack charStack;

    for (int i = 0; i < sentence.length(); i++) {
        char c = sentence[i];

        if (c != ' ') {
            charStack.push(c);
        } else {
            // End of a word — move it to word stack
            if (!charStack.empty()) {
                string word = charStack.popWord();
                sentenceStack.push(word);
            }
        }
    }

    // push last word
    if (!charStack.empty()) {
        string word = charStack.popWord();
        sentenceStack.push(word);
    }

    // Pop and print all words (reversed order)
    while (!sentenceStack.empty()) {
        cout << sentenceStack.pop();
        if (!sentenceStack.empty()) cout << " ";
    }
    cout << endl;
}

// Main
int main() {
    string sentence = "I am from University of Engineering and Technology Lahore";
    cout << "Original: " << sentence << endl;
    cout << "Reversed: ";
    reverseSentence(sentence);
    return 0;
}
