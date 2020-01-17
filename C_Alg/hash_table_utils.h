
typedef struct hash_table{
    char* seq;
    int seq_int;
    int* sequence_index_arr;
    int arr_size;
}hash_table;

hash_table* create_hash_table(int size);
void new_element(hash_table* hash, char* ele, int index);
int pow_2(int base, int power);
int str_to_int(char* str);