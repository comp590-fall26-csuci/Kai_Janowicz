main: main.c fibonacci.c
	gcc main.c fibonacci.c -Iheaders -o main

clean: 
	rm -rf main

tests: fibonacci.c
	gcc test_fib.c fibonacci.c -Iheaders -o run_tests

