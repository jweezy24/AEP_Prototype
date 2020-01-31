#include "main.h"

int main(){

    vn_swap();

}

void vn_swap(){

    int count = 0;
    int count_nums = 0;
    int value = 0;
    int all_nums_pos = 0;


    // This loop creates 2 things.
    // The first thing is a sequence of binary numbers in order of the created array.
    // The second thing this loop does is create a dictionary mapping all the original values

    for(int i=0; i<1000000; i++){
        if (count < 2){
            value += (int)bits[i];
            count+=1;
        }else{

            switch(value){
                case 96:
                    write_to_file("1");
                    break;
                case 98:
                    write_to_file("1");
                    break;
                case 97:
                    write_to_file("0");
                    break;
                }
            
            value = 0;
            count =0;

    }

    }

}

int write_to_file(char* str){
    FILE *fpw;
    //work path
    //fpw = fopen("/opt/sts-2.1.2/sts-2.1.2/data/C_gen_file.txt", "a");
    
    //home
    fpw = fopen("/home/jweezy/Desktop/sts-2.1.2/sts-2.1.2/data/vn_C_gen.txt", "a");
    
    /*Error handling for output file*/
    if (fpw== NULL)
    {
        puts("Issue in opening the Output file");
    }

    fputs(str, fpw);
    fclose(fpw);
    return 0;

}