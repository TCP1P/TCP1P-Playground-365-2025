#include <stdio.h>

int main() {
    FILE *file;
    char flag[100];

    // Open the flag file in read mode
    file = fopen("/root/flag.txt", "r");

    // Check if the file was opened successfully
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Read the flag from the file
    fgets(flag, sizeof(flag), file);

    // Close the file
    fclose(file);

    // Print the flag
    printf("Flag: %s\n", flag);

    return 0;
}
