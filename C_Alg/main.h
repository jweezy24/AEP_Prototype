#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "simulated_input.h"

typedef struct dict{
    char* string;
    int iter;
}dict;

typedef struct bin_number{
    char* seq;
}bin_number;

int main();

char* clear_pointer(char* string);

bin_number* create_bin_number (char* str);

