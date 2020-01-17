import os,sys

def move_files_to_test_area():

    if os.path.isfile("./bin_numbers_after_mapping_raw.bin"):
            os.system("mv ./bin_numbers_after_mapping_raw.bin /home/jweezy/Desktop/sts-2.1.2/data/")
    
    if os.path.isfile("./bin_numbers_after_mapping_bad.bin"):
            os.system("mv ./bin_numbers_after_mapping_bad.bin /home/jweezy/Desktop/sts-2.1.2/data/")

    if os.path.isfile("./bin_numbers_after_mapping.bin"):
            os.system("mv ./bin_numbers_after_mapping.bin /home/jweezy/Desktop/sts-2.1.2/data/")

    if os.path.isfile("./bin_numbers_after_mapping_susan.bin"):
            os.system("mv ./bin_numbers_after_mapping_susan.bin /home/jweezy/Desktop/sts-2.1.2/data/")

    