#!/usr/bin/env bash


python3 ~/ProjectWork/New_Project/Population-Modelling/modules/main.py
#python3 ~/ProjectWork/New_Project/analysis_data/test/test_class.py
gnuplot ~/ProjectWork/New_Project/Population-Modelling/plot.gp

mv *_output.dat ./output