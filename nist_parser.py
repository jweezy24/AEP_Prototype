import os,sys
import numpy as np
import matplotlib.pyplot as plt
import subprocess

def parse_files():
    data_to_file = {}
    for (dirpath, dirnames, filenames) in os.walk('./nist_test_results'):
        for file_name in filenames:
            with open(f'{dirpath}/{file_name}', 'r') as f:
                all_data = []
                for line in f:
                    if '/' in line and '<' not in line:
                        split_line = line.split(' ')
                        data = []
                        for ele in split_line:
                            if ele != '':
                                data.append(ele)
                        all_data.append(data)
                data_to_file[file_name] = all_data
    return data_to_file

def examine_data(data):
    failure_rate = {}
    for key in data:
        passes = 0
        fails = 0
        for ele in data.get(key):
            stars = [i for i, e in enumerate(ele) if e == '*']
            if 12 in stars or 13 in stars:
                fails +=1
            else:
                passes += 1
        failure_rate[key] = (passes/(passes+fails))
    
    return failure_rate


def graph_failure_rate(fail_rates):
    x_axis = list(fail_rates.keys())
    y_axis = [val for key,val in fail_rates.items() ]

    neil_equation = []
    constant_eqation = 0
    vn=False
    for i in range(0,len(x_axis)):
        if "vn" not in x_axis[i]:
            holder = int(x_axis[i].split('_')[-1].replace(".txt", ''))
        else:
            holder = x_axis[i].split('_')[0]
            vn=True
        x_axis[i] = holder
        if not vn:
            neil_equation.append((holder, y_axis[i]))
        else:
            vn = False
            const = y_axis[i]
            constant_eqation_x = np.arange(7)
            constant_eqation_x+=2
            constant_eqation_y = [const]*7
    min_val = 1000
    sorted_eq = []
    tmp = None
    for ele in neil_equation:
        for i in range(0,len(neil_equation)):
            if neil_equation[i][0] < min_val:
                tmp = neil_equation[i]
                min_val = neil_equation[i][0]
                index = i

        if tmp != None:
            sorted_eq.append(tmp)
            neil_equation[index] = (1000,1000)

        min_val = 1000
    zip(*sorted_eq)
    #print(sorted_eq)
    plt.plot(*zip(*sorted_eq), color="red")
    plt.plot(constant_eqation_x, constant_eqation_y, color="blue")
    plt.savefig('nist_success_rate.pdf')


def data_loss_percentage():
    bits = 29478362
    vn_ratio = 1
    tuples = []
    x_vals_neil = []
    y_vals_neil = []
    for filename in os.listdir("./C_Alg/Ascii_files"):
        bits_in_file_str = subprocess.Popen(['wc', '-c', f'./C_Alg/Ascii_files/{filename}'],
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE).communicate()
        


        bits_in_file = int(bits_in_file_str[0].decode('ascii').split(' ')[0])
        

        if 'vn' in filename:
            vn_ratio = bits_in_file/bits
        
        else:
            sequence_length = int(bits_in_file_str[0].decode('ascii').split(' ')[1].split('.')[1].split('/')[-1])
            tmp_ratio = bits_in_file/bits
            index = 0
            tuples.append((sequence_length, tmp_ratio))

    print(tuples)
    sorted_by_sequence = sorted(tuples, key=lambda tup: tup[0])
    print(sorted_by_sequence)
    for seq,val in sorted_by_sequence:
        x_vals_neil.append(seq)
        y_vals_neil.append(val)
    const = vn_ratio
    x_vals_vn = np.arange(len(x_vals_neil)+2)
    y_vals_vn = [const]*(len(y_vals_neil)+2)

    plt.plot(x_vals_vn, y_vals_vn, color="blue")
    plt.plot(x_vals_neil, y_vals_neil, color="red")
    plt.savefig('bit_usage_comparison.pdf')

            
    
if __name__ == '__main__':
    data = parse_files()
    failure_data = examine_data(data)
    graph_failure_rate(failure_data)
    #data_loss_percentage()