#include <stdlib.h>
#include <stdio.h>

struct Node {
    int data;
    struct Node *next;
};

struct Node * create_node(int data) {
    struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
    if (!new_node) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
    }
    new_node->data = data;
    new_node->next = NULL;
    return new_node;
}

void add_node(struct Node **head, int data){
    struct Node *new_node = create_node(data);
    new_node->next = *head;
    *head = new_node;
}

void print_list(struct Node *head) {
    struct Node *current = head;
    while (current) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

void free_list(struct Node *head) {
    struct Node *current = head;
    struct Node *next;
    while (current) {
        next = current->next;
        free(current);
        current = next;
    }
}

int main(){
    struct Node *head = NULL;
    add_node(&head, 1);
    add_node(&head, 2);
    add_node(&head, 3);
    print_list(head);
    add_node(&head, 4);
    print_list(head);
    free_list(head);
    return 0;
}