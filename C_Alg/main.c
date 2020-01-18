#include "main.h"



int main(){

    //hash_table* hasher = create_hash_table(256);
    int count = 0;
    int count_nums = 0;
    int total_bin_nums = (int) (strlen(bits)/9) + 1;
    int total_before_mapping = 512;
    int total_after_mapping = 256;
    bin_number* list_of_binary_seqs = malloc(sizeof(bin_number)*total_bin_nums);
    dict* all_numbers = malloc(sizeof(dict)*total_before_mapping);

    make_inital_bit_sequence(total_bin_nums, list_of_binary_seqs, all_numbers);

    find_highest_half(total_after_mapping, total_before_mapping, all_numbers);

    replace_values(total_before_mapping, total_bin_nums, list_of_binary_seqs, all_numbers);

    remapping_algorithm(total_after_mapping, total_before_mapping, total_bin_nums, list_of_binary_seqs, all_numbers);


}

char* clear_pointer(char* string){
    free(string);
    string = malloc(9);
    return string;
}

bin_number* create_bin_number (char* str){
    bin_number* bin_num = malloc(sizeof(bin_number));
    if (sizeof(str) > 1){
        bin_num->seq = malloc(strlen(str)+1);
        strcpy(bin_num->seq, str);
        return bin_num;
    }else{
        return NULL;
    }
}

int create_dictionary_entry(char* bnum, dict* all_numbers, int iter, int iterate){
    int cont =0;
    if (bnum == NULL){
       return iterate;
    }
    //printf("%s \t %ld\n", bnum, strlen(bnum));
    if (iter>0){
        for(int i=0; i<iter && cont==0; i++){
            ////printf("%d \n", strcmp(all_numbers[i].string, bnum));
            if (all_numbers[i].string == NULL){
                cont = 1;
            }
            if (cont == 0 && strcmp(all_numbers[i].string, bnum) == 0){
                all_numbers[i].iter += 1;
                cont = 1;
                return iterate;
            }
            if(cont == 1){
                all_numbers[i].string = malloc(strlen(bnum)*sizeof(char));
                strcpy(all_numbers[i].string, bnum);
                all_numbers[i].iter = 1;
                return iterate+1;
            }
        }

        if(cont == 0){
            all_numbers[iter].string = malloc(strlen(bnum)*sizeof(char));
            strcpy(all_numbers[iter].string, bnum);
            all_numbers[iter].iter = 1;
            return iterate+1;
        }

    }else{
        all_numbers[iter].string = malloc(strlen(bnum)*sizeof(char));
        strcpy(all_numbers[iter].string, bnum);
        all_numbers[iter].iter = 1;
        return iterate+1;
    }
}

void free_dictionary(dict* all_numbers, int iter){
    for(int i=0; i<iter; i++){
        if (all_numbers[i].string == NULL){
            //free(all_numbers);
            return;
        }
        free(all_numbers[i].string);
    }
    //free(all_numbers);
}

void int_to_binary(char* output_2, int num, int size){
    for(int i = size-1; i >= 0; i--) {
        output_2[i] = (num & 1) + '0';

        num >>= 1;
    }
    

}

void clear_str(char* str, int size){
    free(str);
    str = malloc(size);
}


void make_inital_bit_sequence(int total_bin_nums, bin_number* list_of_binary_seqs, dict* all_numbers){
    int count = 0;
    int count_nums = 0;
    char* bin_num_holder = malloc(10);
    int all_nums_pos = 0;

    // This loop creates 2 things.
    // The first thing is a sequence of binary numbers in order of the created array.
    // The second thing this loop does is create a dictionary mapping all the original values

    for(int i=0; i<total_bin_nums; i++){
        if (count < 9){
            bin_num_holder[count] = bits[i];
            count+=1;
        }else{
            count = 0;
            bin_number* entry = malloc(sizeof(bin_number));
            entry = create_bin_number(bin_num_holder);
            list_of_binary_seqs[count_nums] = *entry;
            all_nums_pos = create_dictionary_entry(entry->seq, all_numbers, all_nums_pos, all_nums_pos);
            bin_num_holder = clear_pointer(bin_num_holder);
            bin_num_holder[count] = bits[i];
            count_nums+=1;
        }
    }
}

void find_highest_half(int total_after_mapping, int total_before_mapping, dict* all_numbers){

    int iter_tmp = 0;
    int max_val = 0;
    max_val = all_numbers[0].iter;

    for(int i=0; i<total_after_mapping; i++){
        for(int j=0; j < total_before_mapping; j++){
            if (max_val < all_numbers[j].iter && all_numbers[j].iter != -1){
                max_val = all_numbers[j].iter;
                iter_tmp = j;
            }

        }
        max_val = -1;
        all_numbers[iter_tmp].iter = -1; 

    }
}

void replace_values(int total_before_mapping, int total_bin_nums, bin_number* list_of_binary_seqs, dict* all_numbers){
    char* replacement_str = "GONE";
    for(int i=0; i<total_before_mapping; i++){
        if(all_numbers[i].iter == -1){
            for(int j=0; j<total_bin_nums; j++){
                if(list_of_binary_seqs[j].seq != NULL && strcmp(replacement_str, list_of_binary_seqs[j].seq) != 0 && 
                    strcmp(list_of_binary_seqs[j].seq, all_numbers[i].string) == 0){
                    clear_str(list_of_binary_seqs[j].seq, strlen(replacement_str));
                    strcpy(list_of_binary_seqs[j].seq, replacement_str);
                }
            }
        }
    }
}

void remapping_algorithm(int total_after_mapping, int total_before_mapping, int total_bin_nums, bin_number* list_of_binary_seqs, dict* all_numbers){
    int iter_tmp = 0;
    int cont = 0;
    int src_size= 0;
    int dest_size = 0;
    char* new_binary_num = malloc(sizeof(char)*9);
    int val = 0;

    for(int i=0; i<total_after_mapping; i++){
        for(int j=0; j < total_before_mapping; j++){
            if (all_numbers[j].iter >= 0 && cont == 0){
                val = all_numbers[j].iter;
                iter_tmp = j;
                cont = 1;

            }
        }
        all_numbers[iter_tmp].iter = -2;
        int_to_binary(new_binary_num, i, 8);
        for(int k=0; k<total_bin_nums; k++){
            if(list_of_binary_seqs[k].seq != NULL && strcmp(all_numbers[iter_tmp].string, list_of_binary_seqs[k].seq) == 0){
                clear_str(list_of_binary_seqs[k].seq, strlen(new_binary_num));
                strcpy(list_of_binary_seqs[k].seq, new_binary_num);  
            }

        cont =0;
        }
        if(i == total_after_mapping-1){
            for(int l=0; l < total_bin_nums; l++){
                clear_str(new_binary_num, 9);
                if(list_of_binary_seqs[l].seq != NULL && strcmp(list_of_binary_seqs[l].seq, "GONE") != 0){
                   write_to_file(list_of_binary_seqs[l].seq);
                }
            }
        }
        clear_str(new_binary_num, 9);

    }

}

int write_to_file(char* str){
    FILE *fpw;
    //work path
    //fpw = fopen("/opt/sts-2.1.2/sts-2.1.2/data/C_gen_file.txt", "a");
    
    //home
    fpw = fopen("/home/jweezy/Desktop/sts-2.1.2/data/C_gen_file.txt", "a");
    
    /*Error handling for output file*/
    if (fpw== NULL)
    {
        puts("Issue in opening the Output file");
    }

    fputs(str, fpw);
    fclose(fpw);
    return 0;

}