#!/usr/bin/env gnuplot

set terminal pngcairo size 1200,800 font "Arial,12"
set title "Population growth of Western Region,Ghana"
set grid
set style line 11 lc rgb "#888888" lt 1 lw 1.5
set grid back ls 11
set xlabel "year"
set ylabel "Population"
set output "./PNG/Western.png"

plot "output.dat" using 1:2 title "." with points lt 7 lc 7 lw 2 dt 1, \
"output.dat" using 1:2 title "Actual Population" smooth csplines with lines lt 7 lc 7 lw 2, \
"output.dat" using 1:3 title "." with points lt 7 lc 9 lw 2 dt 1, \
"output.dat" using 1:3 title "Verhulst" smooth csplines with lines lt 7 lc 9 lw 2, \
"output.dat" using 1:4 title "." with points lt 7 lc 3 lw 2 dt 1, \
"output.dat" using 1:4 title "Gompertz" smooth csplines with lines lt 7 lc 3 lw 2,\
"output.dat" using 1:5 title "." with points lt 7 lc 5 lw 2 dt 1, \
"output.dat" using 1:5 title "Richards" smooth csplines with lines lt 7 lc 5 lw 2
