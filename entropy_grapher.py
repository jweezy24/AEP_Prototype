import matplotlib.pyplot as plt

def parse_data():
    mapped_data = []
    random_data = []
    no_map_data = []
    susan_data = []

    with open('./entropy_mapped.txt', 'r') as f:
        for line in f:
            mapped_data.append((int(line.split('\t')[0]), float(line.split('\t')[1])))
    
    with open('./entropy_random.txt', 'r') as f:
        for line in f:
            random_data.append((int(line.split('\t')[0]), float(line.split('\t')[1])))
    
    with open('./entropy_no_map.txt', 'r') as f:
        for line in f:
            no_map_data.append((int(line.split('\t')[0]), float(line.split('\t')[1])))

    with open('./entropy_susan.txt', 'r') as f:
        for line in f:
            susan_data.append((int(line.split('\t')[0]), float(line.split('\t')[1])))

    entropy_graph([mapped_data, random_data, no_map_data, susan_data])


def entropy_graph(data):
    mapped_data = data[0]
    random_data = data[1]
    no_map_data = data[2]
    susan_data = data[3]



    mapped_x_vals = [x for x,y in mapped_data]
    mapped_y_vals = [y for x,y in mapped_data]

    plt.plot(mapped_x_vals, mapped_y_vals, label="Mapped")

    random_x_vals = [x for x,y in random_data]
    random_y_vals = [y for x,y in random_data]

    plt.plot(random_x_vals, random_y_vals, label="Random")

    no_map_x_vals = [x for x,y in no_map_data]
    no_map_y_vals = [y for x,y in no_map_data]
    
    plt.plot(no_map_x_vals, no_map_y_vals, label="No Map")

    susan_x_vals = [x for x,y in susan_data]
    susan_y_vals = [y for x,y in susan_data]

    plt.plot(susan_x_vals, susan_y_vals, label="Susan")
    plt.legend(loc='best')
    plt.xlabel("Max Number")
    plt.ylabel("Entropy")
    #plt.xlim(120,265)
    #plt.ylim(7,8)

    plt.savefig(f'./entropy.pdf')

def main():
    parse_data()

main()