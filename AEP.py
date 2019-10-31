import random
import math
import array
import os
import scipy.io as mat_parse
import numpy as np
import matplotlib.pyplot as plt
    
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



def examine_stream(stream):
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
                        all_numbers[pos] = count  
            count+=1
        elif val == 0:
            for pos in range(0,len(all_numbers)):
                if type(all_numbers[pos]) == type('t'):
                    if ind == int(all_numbers[pos],2):
                        all_numbers[pos] = -1 
        total_sequences += val

    byte_arr = []
    bin_numbers = []
    count = 0
    if os.path.isfile("./bin_numbers_after_mapping.bin"):
        os.system("rm ./bin_numbers_after_mapping.bin")

    with open('./bin_numbers_after_mapping.bin', 'ab') as f:
        for bin_number in all_numbers:
            if bin_number != -1:
                if count == math.log(map_length,2) and count > 0:
                    print(bin_numbers)
                    num = bytes(bin_numbers)
                    f.write(num)
                    bin_numbers = []
                    count = 0
                else:
                    bin_numbers.append(bin_number)
                    count+=1


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

def examine_stream_no_operations(stream, notRandom):
    count = 0
    num = ''
    numbers = {}
    zero_at = 0
    min_at = 0
    was_appended = False
    last_update = 1
    total_sequences = 0
    start_length = 256
    all_numbers = []
    for i in range(0, start_length):
        numbers[i] = 0

    for val in stream:
        if len(num) == math.log(start_length, 2): 
            bin_num = int(num, 2)
            index = bin_num
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

        if os.path.isfile("./bin_numbers_after_mapping_bad.bin"):
            os.system("rm ./bin_numbers_after_mapping_bad.bin")

        bin_numbers = []
        count = 0
        with open('./bin_numbers_after_mapping_bad.bin', 'ab') as f:
            for bin_number in all_numbers:
                if count == 8 and count > 0:
                    num = bytes(bin_numbers)
                    f.write(num)
                    bin_numbers = []
                    count = 0
                else:
                    bin_numbers.append(bin_number)
                    count+=1
    
    entropy = entropy_calculation(p_set)
        
    # for ind,val in numbers.items():
    #     if val >= 500:
    #         numbers[ind] = 0

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
    os.system("python3 ./sp800_22_tests/sp800_22_tests.py ./bin_numbers_after_mapping_bad.bin")
    os.system("python3 ./sp800_22_tests/sp800_22_tests.py ./bin_numbers_after_mapping.bin")

def main():
    stream_1,stream_2 = stream_parse()
    random_vals_amount = int((len(stream_1)+len(stream_2))/2)
    rand = random_check(random_vals_amount)
    numbers_1 = examine_stream(stream_1)
    numbers_2 = examine_stream_no_operations(stream_2, True)
    numbers_3 = examine_stream_no_operations(rand, False)
    make_histogram(numbers_1,1, "Mapped Data")
    make_histogram(numbers_2,2, "Unmapped Data")
    make_histogram(numbers_3,3, "Completely Random Data")
    preform_nist_tests()




main()