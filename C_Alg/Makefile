

recreate:
	python3 create_simulated_input.py

build:
	gcc -g -o alg.o main.c -lm simulated_input.o

run:
	rm /home/jweezy/Desktop/sts-2.1.2/sts-2.1.2/data/C_gen_file.txt
	touch /home/jweezy/Desktop/sts-2.1.2/sts-2.1.2/data/C_gen_file.txt
	./alg.o 8 /home/jweezy/Desktop/sts-2.1.2/sts-2.1.2/data/C_gen_file.txt
	cp /home/jweezy/Desktop/sts-2.1.2/sts-2.1.2/data/C_gen_file.txt ./ascii_res/code_results.txt
debug:
	gdb -x ef.txt ./alg.o

clean:
	rm ./*.o
	rm ./simulated_input.c
	rm ./code_results.txt

build_v:
	gcc -o vn.o vonnoiman.c

run_v:
	#rm /home/jweezy/Desktop/sts-2.1.2/sts-2.1.2/data/vn_C_gen.txt
	#touch /home/jweezy/Desktop/sts-2.1.2/sts-2.1.2/data/vn_C_gen.txt
	./vn.o
	cp /home/jweezy/Desktop/sts-2.1.2/sts-2.1.2/data/vn_C_gen.txt ./code_results_vn.txt



simulated_input.o:
	gcc -c -o simulated_input.o simulated_input.c
build_ef: simulated_input.o
	gcc -g -o ef.o efficent_main.c simulated_input.o

run_ef:
	rm /home/jweezy/Desktop/sts-2.1.2/sts-2.1.2/data/ef.txt
	./ef.o

debug_ef:
	gdb -x ef.txt ./ef.o
