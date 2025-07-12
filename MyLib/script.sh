#!/usr/bin/env bash


python3 main.py
python3 -m unittest -v 

gnuplot plot.gp
mv ./*_output.dat ../Data