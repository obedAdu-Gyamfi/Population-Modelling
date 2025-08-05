#!/usr/bin/env bash


python3 main.py
python3 -m unittest -v 

mv ./*_output.dat ../Data
gnuplot plot.gp
