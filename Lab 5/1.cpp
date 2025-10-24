#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
    Node(int val) : data(val), next(NULL) {}
};

class LinkList {
private:
    Node* head;

public:
    LinkList() { head = NULL; }
    
    ~LinkList() {
        while (head != NULL) {
            Node* temp = head;
            head = head->next;
            delete temp;
        }
    }
    
    bool isEmpty() { return head == NULL; }
    
    Node* insertAtHead(int x) {
        Node* newNode = new Node(x);
        newNode->next = head;
        head = newNode;
        return head;
    }
    
    Node* insertAtEnd(int x) {
        Node* newNode = new Node(x);
        if (head == NULL) {
            head = newNode;
            return head;
        }
        Node* temp = head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newNode;
        return head;
    }
    
    Node* insertNode(int index, int x) {
        if (index == 0) return insertAtHead(x);
        
        Node* newNode = new Node(x);
        Node* temp = head;
        for (int i = 0; i < index - 1 && temp != NULL; i++) {
            temp = temp->next;
        }
        if (temp == NULL) return NULL;
        
        newNode->next = temp->next;
        temp->next = newNode;
        return head;
    }
    
    bool findNode(int x) {
        Node* temp = head;
        while (temp != NULL) {
            if (temp->data == x) return true;
            temp = temp->next;
        }
        return false;
    }
    
    bool deleteNode(int x) {
        if (head == NULL) return false;
        
        bool deleted = false;
        while (head != NULL && head->data == x) {
            Node* temp = head;
            head = head->next;
            delete temp;
            deleted = true;
        }
        
        Node* current = head;
        while (current != NULL && current->next != NULL) {
            if (current->next->data == x) {
                Node* temp = current->next;
                current->next = current->next->next;
                delete temp;
                deleted = true;
            } else {
                current = current->next;
            }
        }
        return deleted;
    }
    
    bool deleteFromStart() {
        if (head == NULL) return false;
        Node* temp = head;
        head = head->next;
        delete temp;
        return true;
    }
    
    bool deleteFromEnd() {
        if (head == NULL) return false;
        if (head->next == NULL) {
            delete head;
            head = NULL;
            return true;
        }
        Node* temp = head;
        while (temp->next->next != NULL) {
            temp = temp->next;
        }
        delete temp->next;
        temp->next = NULL;
        return true;
    }
    
    void displayList() {
        Node* temp = head;
        while (temp != NULL) {
            cout << temp->data << " -> ";
            temp = temp->next;
        }
        cout << "NULL" << endl;
    }
    
    Node* reverseList() {
        Node* prev = NULL;
        Node* current = head;
        Node* next = NULL;
        
        while (current != NULL) {
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }
        head = prev;
        return head;
    }
    
    Node* sortList(Node* list) {
        if (list == NULL || list->next == NULL) return list;
        
        for (Node* i = list; i != NULL; i = i->next) {
            for (Node* j = i->next; j != NULL; j = j->next) {
                if (i->data > j->data) {
                    int temp = i->data;
                    i->data = j->data;
                    j->data = temp;
                }
            }
        }
        return list;
    }
    
    Node* removeDuplicates(Node* list) {
        if (list == NULL) return NULL;
        
        Node* current = list;
        while (current != NULL && current->next != NULL) {
            if (current->data == current->next->data) {
                Node* temp = current->next;
                current->next = current->next->next;
                delete temp;
            } else {
                current = current->next;
            }
        }
        return list;
    }
    
    Node* mergeLists(Node* list1, Node* list2) {
        if (list1 == NULL) return list2;
        if (list2 == NULL) return list1;
        
        Node* result = NULL;
        if (list1->data <= list2->data) {
            result = list1;
            result->next = mergeLists(list1->next, list2);
        } else {
            result = list2;
            result->next = mergeLists(list1, list2->next);
        }
        return result;
    }
    
    Node* intersectLists(Node* list1, Node* list2) {
        Node* result = NULL;
        Node* tail = NULL;
        
        while (list1 != NULL && list2 != NULL) {
            if (list1->data == list2->data) {
                Node* newNode = new Node(list1->data);
                if (result == NULL) {
                    result = newNode;
                    tail = result;
                } else {
                    tail->next = newNode;
                    tail = tail->next;
                }
                list1 = list1->next;
                list2 = list2->next;
            } else if (list1->data < list2->data) {
                list1 = list1->next;
            } else {
                list2 = list2->next;
            }
        }
        return result;
    }
    
    Node* getHead() { return head; }
};