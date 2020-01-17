

recreate:
	python3 create_simulated_input.py

build:
	gcc -O2 -g -o alg.o main.c

run:
	rm /home/jweezy/Desktop/sts-2.1.2/data/C_gen_file.txt
	touch /home/jweezy/Desktop/sts-2.1.2/data/C_gen_file.txt
	./alg.o
	cp /home/jweezy/Desktop/sts-2.1.2/data/C_gen_file.txt ./code_results.txt

clean:
	rm ./simulated_input.h
	rm ./code_results.txt
