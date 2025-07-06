#!/usr/bin/env bash


python3 ~/KNUST/ProjectWork/New_Project/Population-Modelling/MyLib/main.py
python3 -m unittest -v 
mv ./*_output.dat ../Data

gnuplot ~/KNUST/ProjectWork/New_Project/Population-Modelling/MyLib/plot.gp
#mv -f ./*.json ./JSON
mv -f ./*-Errors.json ./Errors_Analysis
mv -f ./*.json ./JSON