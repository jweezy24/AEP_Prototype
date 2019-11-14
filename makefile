clean:
	rm bin_*
	rm *.txt
single:
	python3 AEP.py true 256

multiple:
	python3 AEP.py false 0

entropy:
	python3 entropy_grapher.py
