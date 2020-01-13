#include "main.h"

int main(){
    char* bin_num_holder = malloc(9);
    int count = 0;
    int count_nums = 0;
    int all_nums_pos = 0;
    int total_bin_nums = (int) (strlen(bits)/9) + 1;
    int total_before_mapping = 512;
    int total_after_mapping = 256;
    bin_number* list_of_binary_seqs = malloc(sizeof(bin_number)*total_bin_nums);
    dict* all_numbers = malloc(sizeof(dict)*total_before_mapping);


    // This loop creates 2 things.
    // The first thing is a sequence of binary numbers in order of the created array.
    // The second thing this loop does is create a dictionary mapping all the original values
    for(int i=0; i<strlen(bits); i++){
        if (count < 9){
            bin_num_holder[count] = bits[i];
        }else{
            count = 0;
            bin_number entry = *create_bin_number(bin_num_holder);
            list_of_binary_seqs[count_nums] = entry;
            all_nums_pos = create_dictionary_entry(entry.seq, all_numbers, all_nums_pos, all_nums_pos);
            bin_num_holder = clear_pointer(bin_num_holder);
            bin_num_holder[count] = bits[i];
            count_nums+=1;
        }
        count+=1;
    }

    int iter_tmp = 0;
    int max_val = 0;
    int cont;
    int val;
    dict* all_numbers_remapped = malloc(sizeof(dict)*total_after_mapping);
    int remapped_iter = 0;
    in_between* remapper = malloc(sizeof(in_between)*total_after_mapping);
    char* new_binary_num = malloc(sizeof(char)*9);
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
    
    iter_tmp = 0;
    for(int i=0; i<256; i++){
        for(int j=0; j < total_before_mapping; j++){
            if (all_numbers[j].iter >= 0 && cont == 0){
                val = all_numbers[j].iter;
                iter_tmp = j;
                cont = 1;

            }
        }
        remapper[remapped_iter].source = malloc(strlen(all_numbers[iter_tmp].string)*sizeof(char)+1);
        remapper[remapped_iter].dest = malloc(strlen(all_numbers[iter_tmp].string)*sizeof(char));
        int_to_binary(new_binary_num, remapped_iter);
        strcpy(remapper[remapped_iter].source, all_numbers[iter_tmp].string);
        strcpy(remapper[remapped_iter].dest, new_binary_num);
        all_numbers[iter_tmp].iter = -2;
        remapped_iter += 1;
        cont =0;
    }
    
    char* tmp_scr = malloc(9);
    char* tmp_dest = malloc(9);
    int total = 0;
    cont=0;

    for(int i=0; i<total_after_mapping; i++){
        strcpy(tmp_scr, remapper[i].source);
        strcpy(tmp_dest, remapper[i].dest);
        for(int j=0; j<total_bin_nums; j++){
            if(list_of_binary_seqs[j].seq != NULL && strcmp(tmp_scr, list_of_binary_seqs[j].seq) == 0){
                clear_str(list_of_binary_seqs[j].seq, strlen(tmp_dest));
                strcpy(list_of_binary_seqs[j].seq, tmp_dest);
                
                total+=1;
            }
        }
    }


    for(int i=0; i< total_bin_nums; i++){
        if(list_of_binary_seqs[i].seq != NULL){
            write_to_file(list_of_binary_seqs[i].seq, strlen(list_of_binary_seqs[i].seq));
        }
    }


    //remap_dictionary_entry(all_numbers[iter_tmp].string, new_binary_num, all_numbers_remapped, remapped_iter, remapper[remapped_iter]);
    
    //PRINTS OUT ALL_NUMBERS VARIABLE
    // for(int j=0; j<total_before_mapping; j++){
    //     printf("%s \t %d \n", all_numbers[j].string, all_numbers[j].iter );
    // }

    //Print Values in mapping table
    // char* str_1 = malloc(sizeof(char)*9);
    // char* str_2 = malloc(sizeof(char)*9);
    // for(int i = 0; i<total_after_mapping; i++){
    //     printf("%s \t %s \n", remapper[i].source, remapper[i].dest);
    //     strcpy(str_2,remapper[i].source);
    //     for(int j=0; j<total_after_mapping; j++){
    //         strcpy(str_1,remapper[j].source);
    //         if(strcmp(str_1,str_2) == 0 && i != j){
    //             printf("BAD\n");
    //         }
    //     }
    // }

    // Prints out the entire sequence edited
    // for(int j=0; j<total_bin_nums; j++){
    //     if(list_of_binary_seqs[j].seq != NULL){
    //         printf("%s", list_of_binary_seqs[j].seq);
    //     }
    
    // }
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

char* int_to_binary(char* output_2, int num){
    for(int i = 7; i >= 0; i--) {
        output_2[i] = (num & 1) + '0';

        num >>= 1;
    }
    return output_2;

}

void clear_str(char* str, int size){
    free(str);
    str = malloc(size);
}

void write_to_file(char* str, int size){
    FILE *fpw;

    fpw = fopen("/home/jweezy/Desktop/sts-2.1.2/data/C_gen_file.txt", "a");

    /*Error handling for output file*/
    if (fpw== NULL)
    {
        puts("Issue in opening the Output file");
    }

    fputs(str, fpw);
    fclose(fpw);
}