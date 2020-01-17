#include "hash_table_utils.h"

hash_table* create_hash_table(int size){
    hash_table* hash = malloc(sizeof(hash_table)*size);
    return hash;
}

void new_element(hash_table* hash, char* ele, int index){
    int val = str_to_int(ele);
    hash[val].seq = malloc((sizeof(char)*strlen(ele))+1);
    hash[val].sequence_index_arr = malloc(sizeof(int));
    strcpy(hash[val].seq, ele);
    hash[val].seq_int = val;
    hash[val].sequence_index_arr[0] = index;
    hash[val].arr_size = 1;
    
}

void add_element(hash_table* hash, char* ele, int index){
    int val = str_to_int(ele);
    hash[val].arr_size +=1;
    hash[val].sequence_index_arr = realloc(hash[val].sequence_index_arr, sizeof(int)*hash[val].arr_size);
    hash[val].sequence_index_arr[hash[val].arr_size-1] = index;
}

int str_to_int(char* str){
    int ret_int = 0;
    int length = strlen(str);

    for(int i=0; i<length; i++){
        if(str[i] == '1'){
            ret_int += pow_2(2,length-(i+1));
            printf("%d\n", pow_2(2,length-(i+1)));
        }
    }

    return ret_int;
}

int pow_2(int base, int power){
    int ret_int = 1;

    for(int i =0; i<power; i++){
        ret_int = ret_int*base;
    }

    return ret_int;

}