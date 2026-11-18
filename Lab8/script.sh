#!/bin/bash


make clean 
make 
make tests

./run_tests
