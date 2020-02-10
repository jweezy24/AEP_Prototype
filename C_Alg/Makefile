

recreate:
	python3 create_simulated_input.py

build:
	gcc -g -o alg.o main.c -lm

run:
	rm /home/jweezy/Desktop/sts-2.1.2/sts-2.1.2/data/C_gen_file.txt
	touch /home/jweezy/Desktop/sts-2.1.2/sts-2.1.2/data/C_gen_file.txt
	./alg.o 8 /home/jweezy/Desktop/sts-2.1.2/sts-2.1.2/data/C_gen_file.txt
	cp /home/jweezy/Desktop/sts-2.1.2/sts-2.1.2/data/C_gen_file.txt ./ascii_res/code_results.txt
debug:
	gdb ./alg.o

clean:
	rm ./*.o
	rm ./simulated_input.h
	rm ./code_results.txt

build_v:
	gcc -o vn.o vonnoiman.c

run_v:
	#rm /home/jweezy/Desktop/sts-2.1.2/sts-2.1.2/data/vn_C_gen.txt
	#touch /home/jweezy/Desktop/sts-2.1.2/sts-2.1.2/data/vn_C_gen.txt
	./vn.o
	cp /home/jweezy/Desktop/sts-2.1.2/sts-2.1.2/data/vn_C_gen.txt ./code_results_vn.txt

build_ef:
	gcc -g -o ef.o efficent_main.c

run_ef:
	rm /home/jweezy/Desktop/sts-2.1.2/sts-2.1.2/data/ef.txt
	./ef.o

debug_ef:
	gdb ./ef.o
