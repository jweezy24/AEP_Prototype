#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "simulated_input.h"
#include "hash_table_utils.c"

typedef struct dict{
    char* string;
    int iter;
}dict;

typedef struct bin_number{
    char* seq;
}bin_number;

typedef struct in_between{
    char* source;
    char* dest;
}in_between;

int main();

int create_dictionary_entry(char* bnum, dict* all_numbers, int iter, int iterate);

char* clear_pointer(char* string);

void free_dictionary(dict* all_numbers, int iter);

bin_number* create_bin_number (char* str);

char* int_to_binary(char* output_2, int num);

dict* remap_dictionary_entry(char* src, char* dest, dict* remapper, int iter, int val);

char* get_key_from_string(dict* all_numbers, char* key);

int fromBinary(char *s);

void clear_str(char* str,int size);

void write_to_file(char* str, int size);