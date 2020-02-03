

recreate:
	python3 create_simulated_input.py

build:
	gcc -g -o alg.o main.c -lm

run:
	rm /home/jweezy/Desktop/sts-2.1.2/sts-2.1.2/data/C_gen_file.txt
	touch /home/jweezy/Desktop/sts-2.1.2/sts-2.1.2/data/C_gen_file.txt
	./alg.o 2 /home/jweezy/Desktop/sts-2.1.2/data/C_gen_file.txt
	cp /home/jweezy/Desktop/sts-2.1.2/sts-2.1.2/data/C_gen_file.txt ./ascii_res/code_results.txt

clean:
	rm ./*.o
	rm ./simulated_input.h
	rm ./code_results.txt

build_v:
	gcc -O2 -o vn.o vonnoiman.c

run_v:
	rm /home/jweezy/Desktop/sts-2.1.2/sts-2.1.2/data/vn_C_gen.txt
	touch /home/jweezy/Desktop/sts-2.1.2/sts-2.1.2/data/vn_C_gen.txt
	./vn.o
	cp /home/jweezy/Desktop/sts-2.1.2/sts-2.1.2/data/vn_C_gen.txt ./code_results_vn.txt
