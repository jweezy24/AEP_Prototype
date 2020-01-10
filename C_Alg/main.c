#include "main.h"

int main(){
    char* bin_num_holder = malloc(9);
    int count = 0;
    int count_nums = 0;
    bin_number* list_of_binary_seqs = malloc(sizeof(bin_number)*1842);
    for(int i=0; i<strlen(bits); i++){
        if (count < 8){
            bin_num_holder[count] = bits[i];
        }else{
            count = 0;
            bin_number entry = *create_bin_number(bin_num_holder);
            list_of_binary_seqs[count_nums] = entry;
            bin_num_holder = clear_pointer(bin_num_holder);
            bin_num_holder[count] = bits[i];
            count_nums+=1;
        }
        count+=1;
    }

    for(int j=0; j<1842; j++){
        printf("%s", list_of_binary_seqs[j].seq);
    }
}

char* clear_pointer(char* string){
    free(string);
    string = malloc(9);
    return string;
}

bin_number* create_bin_number (char* str){
    bin_number* bin_num = malloc(sizeof(bin_number));
    bin_num->seq = malloc(sizeof(str));
    strcpy(bin_num->seq, str);
    return bin_num;
}
