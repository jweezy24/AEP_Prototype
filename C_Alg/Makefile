

recreate:
	python3 create_simulated_input.py
	
run:
	gcc -O2 -o alg.o main.c
	rm /home/jweezy/Desktop/sts-2.1.2/data/C_gen_file.txt
	touch /home/jweezy/Desktop/sts-2.1.2/data/C_gen_file.txt
	./alg.o
	cp /home/jweezy/Desktop/sts-2.1.2/data/C_gen_file.txt ./code_results.txt

clean:
	rm ./simulated_input.h
	rm ./code_results.txt
