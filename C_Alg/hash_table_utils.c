
hash_table* create_hash_table(){
    hash_table* hash = malloc(sizeof(hash_table));
    return hash_table;
}

void new_element(hash_table* hash, char* ele, int index){
    hash->seq = malloc((sizeof(char)*strlen(ele))+1);
    hash->sequence_index_arr = malloc(sizeof(int));
    strcpy(hash->seq, ele);

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