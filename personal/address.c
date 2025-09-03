# include <stdio.h>
# include <stdlib.h>

struct Address {
    char name[20];
    char phone[15];
    char email[30];
};

void printAllAddresses(struct Address *addresses, int count) {
    for (int i = 0; i < count; i++) {
        printf("Name: %s\n", addresses[i].name);
        printf("Phone: %s\n", addresses[i].phone);
        printf("Email: %s\n", addresses[i].email);
        printf("-------------------------\n");
    }
}

void deleteAddress(struct Address *addresses, int index, int *count) {
    if (index < 0 || index >= *count) {
        printf("Invalid index.\n");
        return;
    }
    for (int i = index; i < *count - 1; i++) {
        addresses[i] = addresses[i + 1];
    }
    (*count)--;
}

void saveAddressToFiles(struct Address *addresses, int count) {
    FILE *file = fopen("addresses.txt", "w");
    if (!file) {
        printf("Error opening file for writing.\n");
        return;
    }
    for (int i = 0; i < count; i++) {
        fprintf(file, "Name: %s\n", addresses[i].name);
        fprintf(file, "Phone: %s\n", addresses[i].phone);
        fprintf(file, "Email: %s\n", addresses[i].email);
        fprintf(file, "-------------------------\n");
    }
    fclose(file);
}

void addAddress(struct Address *addresses, int count) {
    if (count >= 100) {
        printf("Address book is full.\n");
        return;
    }
    struct Address newAddress;
    printf("Enter name: ");
    scanf("%19s", newAddress.name);
    printf("Enter phone: ");
    scanf("%14s", newAddress.phone);
    printf("Enter email: ");
    scanf("%29s", newAddress.email);
    addresses[count] = newAddress;
}

void loadAddressFromFile(struct Address *addresses, int *count) {
    FILE *file = fopen("addresses.txt", "r");
    if (!file) {
        printf("Error opening file for reading.\n");
        return;
    }
    while (fscanf(file, "Name: %19s\n", addresses[*count].name) == 1) {
        fscanf(file, "Phone: %14s\n", addresses[*count].phone);
        fscanf(file, "Email: %29s\n", addresses[*count].email);
        (*count)++;
    }
    fclose(file);
}

int main() {
    struct Address book[100];
    int count = 0;
    loadAddressFromFile(book, &count);
    while (1) {
        printf("1. Add Address\n");
        printf("2. Delete Address\n");
        printf("3. Print All Addresses\n");
        printf("4. Save Addresses to File\n");
        printf("5. Exit\n");
        printf("Choose an option: ");
        int choice;
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                addAddress(book, count);
                count++;
                break;
            case 2:
                printf("Enter index to delete: ");
                int index;
                scanf("%d", &index);
                deleteAddress(book, index, &count);
                break;
            case 3:
                printAllAddresses(book, count);
                break;
            case 4:
                saveAddressToFiles(book, count);
                break;
            case 5:
                exit(0);
            default:
                printf("Invalid choice.\n");
        }
    }
}