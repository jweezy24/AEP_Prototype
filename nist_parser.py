import os,sys
import matplotlib.pyplot as plt

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
    for i in range(0,len(x_axis)):
        holder = x_axis[i].split('_')[0]
        x_axis[i] = holder
    plt.bar(x_axis, y_axis)
    plt.savefig('nist_success_rate.pdf')

if __name__ == '__main__':
    data = parse_files()
    failure_data = examine_data(data)
    graph_failure_rate(failure_data)