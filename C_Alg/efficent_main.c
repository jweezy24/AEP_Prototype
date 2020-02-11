#include "main.h"

//#define DEBUG 

extern char bits[];

int bl = 9;
int sl = 8;
int total_bin_nums = 29478361;
int total_before_mapping = 512;
int total_after_mapping = 256;

int main(){
    int total_before_mapping = pow_jack(2,bl);
    int total_after_mapping = pow_jack(2,sl);
    int count = 0;
    int j;

    int list_ints_before[512] = {};
    int list_ints_after[256] = {};
    int judges_list[512] = {};
    int ordering_list_before[512] ={};
    int ordering_list_after[256] = {};

    char *path = "/home/jack-admin/Desktop/sts-2.1.2/sts-2.1.2/data/ef.txt"; 

    for(j = 0; j < total_before_mapping; j++){
        list_ints_before[j] = 0;
    }

    for(j = 0; j < total_after_mapping; j++){
        list_ints_after[j] = 0;
    }

    for(j = 0; j < total_before_mapping; j++){
        judges_list[j] = 0;
    }

    for(j = 0; j < total_before_mapping; j++){
        ordering_list_before[j] = -1;
    }

    for(j = 0; j < total_after_mapping; j++){
        ordering_list_after[j] = -1;
    }


    int number = 0;
    int current_number = 0;
    int nxt = 0;
    int digit = 0;
    int accum = 1;

    for(j = 0; j < 29478361;){
        if(count < 9){
	    if (count == 0 && bits[j]=='1'){
	    	accum=0;
		current_number+=1;
	    }else if(count == 0){
	    	accum=0;
	    }
	    if (count ==1){
	    	accum=1;
	    }
            if (bits[j] == '1'){
               digit = 1;
	       accum*= 2;
            }else if(bits[j] == '0'){
	    	digit = 0;
		accum*=2;
	    }
	    current_number += accum*digit;
	    count+=1;
            j++;
        }else{
#ifdef DEBUG
	    printf("j=%d\n", j);
#endif
            count = 0;
            list_ints_before[current_number] += 1;
            if(ordering_list_before[current_number] == -1){
                ordering_list_before[current_number] = nxt;
                nxt+=1;
            }
            current_number = 0;
            number = 0;
	    accum=1;
        }
    }

    int tmp = 0;
    for(int i = 0; i < total_before_mapping; i++){
    	tmp += list_ints_before[i];
    }

    int current_check = 0;
    int  greater_than = 0;

    for(int i = 0; i < total_before_mapping; i++){
        current_check = list_ints_before[i];
        for(int j = 0; j < total_before_mapping; j++){
            if(current_check > list_ints_before[j]){
                greater_than += 1; 
            }
        }
        judges_list[i] = greater_than;
        greater_than = 0;   
    }

    current_check = 0;
    greater_than = 0;
    int dropped = 255;
    int cont = 1;
    //Extracting the highest half of numbers
    //
    for(int i = 0; i < total_after_mapping; i++){
        for(int j = 0; j < total_before_mapping; j++){
            if(current_check <= judges_list[j] && judges_list[j] != -1 && i!=j){
                current_check = judges_list[j];
                cont = j;
            }
        }

        
        list_ints_before[cont] = -1;
        judges_list[cont] = -1;
        ordering_list_before[cont] = -1;
        current_check = 0;
    }

    int iter = 0;
    current_check = 512;
    int val = 0;
    int order_iter=0;
    int check = 0;

    for(int i =0; i < total_after_mapping; i++){
        for(int j = 0; j < total_before_mapping; j++){
            if(current_check > ordering_list_before[j] && ordering_list_before[j] != -1 && check == 0){
                current_check = ordering_list_before[j];
                val = current_check;
                ordering_list_before[j] = -1;
		check = 1;
            }
        }
        ordering_list_after[order_iter] = val;
        order_iter+=1;
        current_check = 512;
	check = 0;
    }

    for(int i =0; i < total_before_mapping; i++){
        
        if(list_ints_before[i] != -1){
            list_ints_after[iter] = ordering_list_after[i];
            iter+=1;
        }
    }

    int remapped_number = 0;
    int pos_holder = 0;
    int mapped =0;  
    count = 0;
    current_number = 0;
    int converter = total_after_mapping;
    number = 0;

    for(int i = 0; i < total_bin_nums;){
        if(count < bl){
            if (bits[i] == '1'){
                number = pow_jack(2, count);
                current_number += number;
            }
            if(current_number > 511){
                printf("FUCK UP ALRET");
            }
            count+=1;
            i++;
        }else{
            mapped = 0;
            pos_holder = (i) - count;
            for(int j = 0; j < total_after_mapping; j++){
                if(current_number == list_ints_after[j]){
                    remapped_number = j;
                    mapped = 1;
                }
            }

            if(mapped == 0){
                for(int j = 0; j < bl; j++) {
                    bits[pos_holder+j] = 0;

                }
            }else{
                //converts integer into 8 bit binary sequence within the given list.
                for(int j = 8; j >=0; j--) {
                    bits[(pos_holder)+j] = (remapped_number & 1) + '0';
                    remapped_number <<= 1;
                }
            }
            bits[i-1] = 0;
            current_number = 0;
            remapped_number = 0;
            pos_holder = 0;
            count = 0;

        }
    }

    write_to_file(bits, path);


}



int str_int(char* str){
    char c = 0;
    int tmp_num = 0;
    int num = 0;
    int size = strlen(str);

    for (int i =0; i < size; i++){
        c = str[i];
        tmp_num = c -'0';
        num += tmp_num*pow_jack(10, size-(i+1));   
    }
    return num;
}

int pow_jack(int a, int b){
    int tmp_num = 1;
    if (b == 0){
        return 1;
    }
    for(int i = 0; i < b; i++){
        tmp_num = tmp_num*a;
    }
    return tmp_num;
}

int write_to_file(char* str, char* path){
    FILE *fpw;
    //work path
    //fpw = fopen("/opt/sts-2.1.2/sts-2.1.2/data/C_gen_file.txt", "a");
    
    //laptop
    fpw = fopen(path, "a");
    
    /*Error handling for output file*/
    if (fpw== NULL)
    {
        puts("Issue in opening the Output file");
    }

    for(int i = 0; i < total_bin_nums; i++){
        if(str[i] != 0){
            fputc(str[i], fpw);
        }
    }
    fclose(fpw);
    return 0;

}