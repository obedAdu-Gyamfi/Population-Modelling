#!/usr/bin/env bash


python3 ~/KNUST/ProjectWork/New_Project/Population-Modelling/MyLib/main.py
python3 -m unittest -v 

gnuplot ~/KNUST/ProjectWork/New_Project/Population-Modelling/MyLib/plot.gp
mv ./*_output.dat ../Data