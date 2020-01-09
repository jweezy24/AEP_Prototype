import random
import math
import array
import os
import time
import scipy.io as mat_parse
import numpy as np
import matplotlib.pyplot as plt
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("holder")
parser.add_argument("size")
args = parser.parse_args()
    
def stream_parse():
    binary_data = mat_parse.loadmat('after_correction_256.mat')
    darray_bin = binary_data['after_correction_256']
    rows = darray_bin.shape[0]
    cols = darray_bin.shape[1]
    data_1 = []
    data_2 = []
    for x in range(rows-1, -1, -1):
        for y in range(cols-1, -1, -1):
            if y%2 == 0:
                data_1.append(darray_bin[x,y])
            else:
                data_2.append(darray_bin[x,y])
    return (data_1, data_2)

def bits_log_parse():
    bits = []
    with open('./bits.log', 'r') as f:
        for line in f:
            bits.append(line[0])
    print(len(bits))
    return bits

def random_check(vals):
    random_set = []
    for i in range(0, vals):
        test_num = random.randint(0,128)
        random_set.append(str(test_num%2))
    return random_set

def entropy_calculation(p_set):
    total = 0
    for ele in p_set:
        total += math.log(ele,2)*ele
    
    return -total

def susan_changes(stream):
    sequence = []
    num = ''
    for val in stream:
        if len(num) == 2:
            if num == '11' or num == '00':
                num = ''
            else:
                if num == '10':
                    sequence.append('0')
                elif num == '01':
                    sequence.append('1')
                num = ''
        else:
            num += str(val)
    return sequence

def sequence_counter(string):
    was_0 = False
    was_1 = False
    seq = 0
    max_seq = 0
    for letter in string:
        if not was_0 and not was_1:
            seq = 1
            if letter == '1':
                was_1 = True
            elif letter == '0':
                was_0 = True
            continue

        if was_0 and letter == '0':
            seq += 1
            was_1 = False

        elif was_1 and letter == '1':
            seq += 1
            was_0 = False
        
        elif was_0 and letter == '1':
            if seq > max_seq:
                max_seq = seq
            seq = 1
            was_0 = False
            was_1 = True

        elif was_1 and letter == '0':
            if seq > max_seq:
                max_seq = seq
            seq = 1
            was_1 = False
            was_0 = True

    if max_seq < seq:
        max_seq = seq

    return max_seq



def examine_stream_ascii(stream, isSusan):
    count = 0
    num = ''
    numbers = {}
    zero_at = 0
    min_at = 0
    was_appended = False
    last_update = 1
    total_sequences = 0
    start_length = 512
    map_length = start_length/2
    all_numbers = []

    for i in range(0,start_length):
        numbers[i] = 0

    for val in stream:
        if len(num) == math.log(start_length, 2): 
            bin_num = int(num, 2)
            index = bin_num
            numbers[index] = numbers[index]+1

            all_numbers.append(num)

            #was_appended = False
            num = ''

        else:
            num += str(val)
        count+=1

        max_val = 0
        max_val_2 = 0
        max_ind = 0
        max_ind_2 = 0

    for ind,val in numbers.items():
        if max_val < val:
            max_val = val
            max_ind = ind
        if max_val_2 < val and val < max_val:
            max_val_2 = val
            max_ind_2 = ind


    #for
    total_elements = len(numbers.items())
    local_max = 0
    local_ind = 0
    min_cut_count = 4
    while total_elements > map_length:
        local_max = 0
        local_ind = 0   
        local_min = 1000000000
        local_ind_min = 0 
        for ind,val in numbers.items():
            if local_max < val:
                local_max = val
                local_ind = ind
            if local_min > val:
                local_ind_min = ind
                local_min = val
        if total_elements > map_length and local_max != 0:
            numbers[local_ind] = 0
            total_elements -= 1
    
    new_numbers = {}
    count = 0

    for ind,val in numbers.items():
        if val > 0:
            new_numbers[count] = val
            for pos in range(0,len(all_numbers)):
                if type(all_numbers[pos]) == type('t'):
                    if ind == int(all_numbers[pos],2):
                        str_numb = '{0:09b}'.format(count)
                        all_numbers[pos] = '{0:09b}'.format(count)  
            count+=1
        elif val == 0:
            for pos in range(0,len(all_numbers)):
                if type(all_numbers[pos]) == type('t'):
                    if ind == int(all_numbers[pos],2):
                        all_numbers[pos] = -1 
        total_sequences += val
    
    with open('./bin_numbers_after_mapping.txt', 'a') as f:
        for bin_number in all_numbers:
            if bin_number != -1:
                f.write(bin_number)

    p_set = []
    for ind,val in new_numbers.items():
        k = val/total_sequences
        p_set.append(k)
    
    entropy = entropy_calculation(p_set)
        
    # for ind,val in numbers.items():
    #     if val >= 500:
    #         numbers[ind] = 0

    print(f'{max_ind}\t{max_ind_2}\t{entropy}')    

    return new_numbers

def examine_stream_binary(stream, isSusan, size,iter):
    count = 0
    num = ''
    numbers = {}
    zero_at = 0
    min_at = 0
    was_appended = False
    last_update = 1
    total_sequences = 0
    start_length = size
    map_length = start_length/2
    all_numbers = []

    for i in range(0,start_length):
        binary_str = "{0:#b}".format(i)[2:]
        numbers[binary_str] = 0

    for val in stream:
        if len(num) == math.log(start_length, 2): 
            try:
                bin_num = int(num,2)
                
            except:
                num = ''
                continue
            index = "{0:#b}".format(bin_num)[2:]
            numbers[index] = numbers[index]+1
            
            all_numbers.append(num)

            #was_appended = False
            num = ''

        else:
            num += str(val)
        count+=1

        max_val = 0
        max_val_2 = 0
        max_ind = 0
        max_ind_2 = 0

    for ind,val in numbers.items():
        if max_val < val:
            max_val = val
            max_ind = ind
        if max_val_2 < val and val < max_val:
            max_val_2 = val
            max_ind_2 = ind


    #for
    total_elements = len(numbers.items())
    local_max = 0
    local_ind = 0
    min_cut_count = 4
    if not isSusan:
        while total_elements > map_length:
            local_max = 0
            local_ind = 0   
            local_min = 1000000000
            local_ind_min = 0 
            for ind,val in numbers.items():
                if local_max < val:
                    local_max = val
                    local_ind = ind
                if local_min > val:
                    local_ind_min = ind
                    local_min = val
            if total_elements > map_length and local_max != 0:
                numbers[local_ind] = 0
                total_elements -= 1
    
    new_numbers = {}
    count = 0
    #print(numbers)

    for ind,val in numbers.items():
        if val > 0:
            new_numbers[count] = val
            for pos in range(0,len(all_numbers)):
                if type(all_numbers[pos]) == type('t'):
                    tmp_holder = int(all_numbers[pos],2)
                    cmp_val = "{0:#b}".format(tmp_holder)[2:]
                    if ind == cmp_val:
                        holder = "{0:#b}".format(count)[2:]
                        if len(holder) < math.log(map_length, 2):
                            zeros = math.log(map_length, 2)-len(holder)
                            str_0 = ''
                            for i in range(0,int(zeros)):
                                str_0 += '0'
                            all_numbers[pos] = str_0+holder
                        else:
                            all_numbers[pos] = holder
            count+=1
        elif val == 0:
            for pos in range(0,len(all_numbers)):
                if type(all_numbers[pos]) == type('t'):
                    tmp_holder = int(all_numbers[pos],2)
                    cmp_val = "{0:#b}".format(tmp_holder)[2:]
                    if ind == cmp_val:
                        all_numbers[pos] = -1 
        total_sequences += val
    
    #print(new_numbers)
    byte_arr = []
    bin_numbers = []
    count = 0

    if not isSusan:
        file_name = f'./bin_numbers_after_mapping_{iter}.txt'
    else:
        file_name = f'./bin_numbers_after_mapping_susan_{iter}.txt'

    with open(file_name, 'a') as f:
        for bin_number in all_numbers:
            if bin_number != -1:
                # if count == math.log(map_length,2) and count > 0:
                #     num = bytes(bin_numbers)
                #     f.write(num)
                #     bin_numbers = []
                #     count = 0
                # else:
                #     bin_numbers.append(bin_number)
                #     count+=1
                f.write(bin_number.replace('\n',''))

    p_set = []
    for ind,val in new_numbers.items():
        k = val/total_sequences
        p_set.append(k)
    
    entropy = entropy_calculation(p_set)
        
    # for ind,val in numbers.items():
    #     if val >= 500:
    #         numbers[ind] = 0

    if not isSusan:
        with open('entropy_mapped.txt', 'a') as f:
            f.write(f'{int(size/2)}\t{entropy}\n')
    else:
        with open('entropy_susan.txt', 'a') as f:
            f.write(f'{size}\t{entropy}\n')

    print(f'{max_ind}\t{max_ind_2}\t{entropy}')    

    return new_numbers

def examine_stream_no_operations(stream, notRandom,size,iter):
    count = 0
    num = ''
    numbers = {}
    zero_at = 0
    min_at = 0
    was_appended = False
    last_update = 1
    total_sequences = 0 
    start_length = size
    all_numbers = []
    for i in range(0, start_length):
        binary_str = "{0:#b}".format(i)[2:]
        numbers[binary_str] = 0

    for val in stream:
        if len(num) == math.log(start_length, 2): 
            try:
                bin_num = int(num,2)
            except:
                num = ''
                continue
            index = "{0:#b}".format(bin_num)[2:]
            numbers[index] = numbers[index]+1
            all_numbers.append(index)
            total_sequences += 1
            num = ''

        else:
            num += str(val)
        count+=1

        max_val = 0
        max_val_2 = 0
        max_ind = 0
        max_ind_2 = 0

    p_set = []
    for ind,val in numbers.items():
        k = val/total_sequences
        p_set.append(k)


    if notRandom:

        if os.path.isfile(f"./bin_numbers_no_map_{iter}.txt"):
            os.system(f"rm ./bin_numbers_no_map_{iter}.txt")

        bin_numbers = []
        count = 0
        with open(f'./bin_numbers_no_map_{iter}.txt', 'a') as f:
            for bin_number in all_numbers:
                # if count == math.log(start_length,2) and count > 0:
                #     num = bytes(bin_numbers)
                #     f.write(num)
                #     bin_numbers = []
                #     count = 0
                # else:
                #     bin_numbers.append(bin_number)
                #     count+=1
                f.write(bin_number)

    else:

        if os.path.isfile(f"./bin_numbers_after_mapping_pyrandom_{iter}.txt"):
            os.system(f"rm ./bin_numbers_after_mapping_pyrandom_{iter}.txt")

        bin_numbers = []
        count = 0
        with open(f'./bin_numbers_after_mapping_pyrandom_{iter}.txt', 'a') as f:
            for bin_number in all_numbers:
                # if count == math.log(start_length,2) and count > 0:
                #     num = bytes(bin_numbers)
                #     f.write(num)
                #     bin_numbers = []
                #     count = 0
                # else:
                #     bin_numbers.append(bin_number)
                #     count+=1
                f.write(bin_number)
    
    entropy = entropy_calculation(p_set)
        
    # for ind,val in numbers.items():
    #     if val >= 500:
    #         numbers[ind] = 0

    if notRandom:
        with open('entropy_no_map.txt', 'a') as f:
            f.write(f'{size}\t{entropy}\n')
    else:
        with open('entropy_random.txt', 'a') as f:
            f.write(f'{size}\t{entropy}\n')

    print(f'{max_ind}\t{max_ind_2}\t{entropy}')    

    return numbers

def make_histogram(vals,num, name):
    entries = [(k, v) for k, v in vals.items()] 

    x_vals = [x for x,y in entries]
    y_vals = [y for x,y in entries]
    plt.bar(x_vals, y_vals)
    plt.title(name)
    plt.xlabel("Binary Number Formed By Sequence")
    plt.ylabel("Number of Entries")

    plt.savefig(f'./plot_{name.replace(" ", "_")}.pdf')
    plt.clf()


def preform_nist_tests():
    os.system("python3 ./sp800_22_tests/sp800_22_tests.py ./bin_numbers_after_mapping_bad.bin >> bin_test_results_bad.txt")
    os.system("python3 ./sp800_22_tests/sp800_22_tests.py ./bin_numbers_after_mapping.bin >> bin_test_results.txt")
    os.system("python3 ./sp800_22_tests/sp800_22_tests.py ./bin_numbers_after_mapping_susan.bin >> bin_test_results_susan.txt")

def main():
    is_individual = args.holder
    stream_1,stream_2 = stream_parse()
    stream_3 = susan_changes(stream_1)
    stream_4 = bits_log_parse()
    random_vals_amount = len(stream_4)
    stream_5 = susan_changes(stream_4)
    rand = random_check(random_vals_amount)
    if is_individual != 'true':
        for i in range(2,10):
            iter =i
            size = int(math.pow(2, i))
            print(size)
            numbers_1 = examine_stream_binary(stream_4,False,size*2,iter)
            numbers_1_s = examine_stream_binary(stream_5,True,size,iter)
            numbers_2 = examine_stream_no_operations(stream_4, True,size,iter)
            numbers_3 = examine_stream_no_operations(rand, False,size,iter)
    else:
        size = int(args.size)
        numbers_1 = examine_stream_binary(stream_4,False,size*2,8)
        numbers_1_s = examine_stream_binary(stream_5,True,size,8)
        numbers_2 = examine_stream_no_operations(stream_4, True,size,8)
        numbers_3 = examine_stream_no_operations(rand, False,size,8)
    make_histogram(numbers_1,1, "Mapped Data")
    make_histogram(numbers_2,2, "Unmapped Data")
    make_histogram(numbers_3,3, "Completely Random Data")
    make_histogram(numbers_1_s,4, "Mapped Data Susan Method")
    preform_nist_tests()




main()