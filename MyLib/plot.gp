#!/usr/bin/env gnuplot

set terminal pngcairo size 1200,800 font "Arial,12"
set title "Population growth of Western Region,Ghana"
set grid
set style line 11 lc rgb "#888888" lt 1 lw 1.5
set grid back ls 11
set xlabel "year"
set ylabel "Population"
set output"../PNG/Western.png"

plot "../Data/Western_output.dat" using 1:2 title "." with points lt 7 lc 7 lw 2 dt 1, \
"../Data/Western_output.dat" using 1:2 title "Actual Population" smooth csplines with lines lt 7 lc 7 lw 2, \
"../Data/Western_output.dat" using 1:3 title "." with points lt 7 lc 9 lw 2 dt 1, \
"../Data/Western_output.dat" using 1:3 title "Verhulst" smooth csplines with lines lt 7 lc 9 lw 2, \
"../Data/Western_output.dat" using 1:4 title "." with points lt 7 lc 3 lw 2 dt 1, \
"../Data/Western_output.dat" using 1:4 title "Gompertz" smooth csplines with lines lt 7 lc 3 lw 2,\
"../Data/Western_output.dat" using 1:5 title "." with points lt 7 lc 5 lw 2 dt 1, \
"../Data/Western_output.dat" using 1:5 title "Richards" smooth csplines with lines lt 7 lc 5 lw 2

set terminal pngcairo size 1200,800 font "Arial,12"
set title "Population growth of Central Region,Ghana"
set grid
set style line 11 lc rgb "#888888" lt 1 lw 1.5
set grid back ls 11
set xlabel "year"
set ylabel "Population"
set output "../PNG/Central.png"

plot "../Data/Central_output.dat" using 1:2 title "." with points lt 7 lc 7 lw 2 dt 1, \
"../Data/Central_output.dat" using 1:2 title "Actual Population" smooth csplines with lines lt 7 lc 7 lw 2, \
"../Data/Central_output.dat" using 1:3 title "." with points lt 7 lc 9 lw 2 dt 1, \
"../Data/Central_output.dat" using 1:3 title "Verhulst" smooth csplines with lines lt 7 lc 9 lw 2, \
"../Data/Central_output.dat" using 1:4 title "." with points lt 7 lc 3 lw 2 dt 1, \
"../Data/Central_output.dat" using 1:4 title "Gompertz" smooth csplines with lines lt 7 lc 3 lw 2,\
"../Data/Central_output.dat" using 1:5 title "." with points lt 7 lc 5 lw 2 dt 1, \
"../Data/Central_output.dat" using 1:5 title "Richards" smooth csplines with lines lt 7 lc 5 lw 2


set terminal pngcairo size 1200,800 font "Arial,12"
set title "Population growth of Greater Accra Region,Ghana"
set grid
set style line 11 lc rgb "#888888" lt 1 lw 1.5
set grid back ls 11
set xlabel "year"
set ylabel "Population"
set output "../PNG/GreaterAccra.png"

plot "../Data/GreaterAccra_output.dat" using 1:2 title "." with points lt 7 lc 7 lw 2 dt 1, \
"../Data/GreaterAccra_output.dat" using 1:2 title "Actual Population" smooth csplines with lines lt 7 lc 7 lw 2, \
"../Data/GreaterAccra_output.dat" using 1:3 title "." with points lt 7 lc 9 lw 2 dt 1, \
"../Data/GreaterAccra_output.dat" using 1:3 title "Verhulst" smooth csplines with lines lt 7 lc 9 lw 2, \
"../Data/GreaterAccra_output.dat" using 1:4 title "." with points lt 7 lc 3 lw 2 dt 1, \
"../Data/GreaterAccra_output.dat" using 1:4 title "Gompertz" smooth csplines with lines lt 7 lc 3 lw 2,\
"../Data/GreaterAccra_output.dat" using 1:5 title "." with points lt 7 lc 5 lw 2 dt 1, \
"../Data/GreaterAccra_output.dat" using 1:5 title "Richards" smooth csplines with lines lt 7 lc 5 lw 2

set terminal pngcairo size 1200,800 font "Arial,12"
set title "Population growth of Volta Region,Ghana"
set grid
set style line 11 lc rgb "#888888" lt 1 lw 1.5
set grid back ls 11
set xlabel "year"
set ylabel "Population"
set output "../PNG/Volta.png"

plot "../Data/Volta_output.dat" using 1:2 title "." with points lt 7 lc 7 lw 2 dt 1, \
"../Data/Volta_output.dat" using 1:2 title "Actual Population" smooth csplines with lines lt 7 lc 7 lw 2, \
"../Data/Volta_output.dat" using 1:3 title "." with points lt 7 lc 9 lw 2 dt 1, \
"../Data/Volta_output.dat" using 1:3 title "Verhulst" smooth csplines with lines lt 7 lc 9 lw 2, \
"../Data/Volta_output.dat" using 1:4 title "." with points lt 7 lc 3 lw 2 dt 1, \
"../Data/Volta_output.dat" using 1:4 title "Gompertz" smooth csplines with lines lt 7 lc 3 lw 2,\
"../Data/Volta_output.dat" using 1:5 title "." with points lt 7 lc 5 lw 2 dt 1, \
"../Data/Volta_output.dat" using 1:5 title "Richards" smooth csplines with lines lt 7 lc 5 lw 2

set terminal pngcairo size 1200,800 font "Arial,12"
set title "Population growth of Eastern Region,Ghana"
set grid
set style line 11 lc rgb "#888888" lt 1 lw 1.5
set grid back ls 11
set xlabel "year"
set ylabel "Population"
set output "../PNG/Eastern.png"

plot "../Data/Eastern_output.dat" using 1:2 title "." with points lt 7 lc 7 lw 2 dt 1, \
"../Data/Eastern_output.dat" using 1:2 title "Actual Population" smooth csplines with lines lt 7 lc 7 lw 2, \
"../Data/Eastern_output.dat" using 1:3 title "." with points lt 7 lc 9 lw 2 dt 1, \
"../Data/Eastern_output.dat" using 1:3 title "Verhulst" smooth csplines with lines lt 7 lc 9 lw 2, \
"../Data/Eastern_output.dat" using 1:4 title "." with points lt 7 lc 3 lw 2 dt 1, \
"../Data/Eastern_output.dat" using 1:4 title "Gompertz" smooth csplines with lines lt 7 lc 3 lw 2,\
"../Data/Eastern_output.dat" using 1:5 title "." with points lt 7 lc 5 lw 2 dt 1, \
"../Data/Eastern_output.dat" using 1:5 title "Richards" smooth csplines with lines lt 7 lc 5 lw 2


set terminal pngcairo size 1200,800 font "Arial,12"
set title "Population growth of Ashanti Region,Ghana"
set grid
set style line 11 lc rgb "#888888" lt 1 lw 1.5
set grid back ls 11
set xlabel "year"
set ylabel "Population"
set output "../PNG/Ashanti.png"

plot "../Data/Ashanti_output.dat" using 1:2 title "." with points lt 7 lc 7 lw 2 dt 1, \
"../Data/Ashanti_output.dat" using 1:2 title "Actual Population" smooth csplines with lines lt 7 lc 7 lw 2, \
"../Data/Ashanti_output.dat" using 1:3 title "." with points lt 7 lc 9 lw 2 dt 1, \
"../Data/Ashanti_output.dat" using 1:3 title "Verhulst" smooth csplines with lines lt 7 lc 9 lw 2, \
"../Data/Ashanti_output.dat" using 1:4 title "." with points lt 7 lc 3 lw 2 dt 1, \
"../Data/Ashanti_output.dat" using 1:4 title "Gompertz" smooth csplines with lines lt 7 lc 3 lw 2,\
"../Data/Ashanti_output.dat" using 1:5 title "." with points lt 7 lc 5 lw 2 dt 1, \
"../Data/Ashanti_output.dat" using 1:5 title "Richards" smooth csplines with lines lt 7 lc 5 lw 2


set terminal pngcairo size 1200,800 font "Arial,12"
set title "Population growth of Brong Ahafo Region,Ghana"
set grid
set style line 11 lc rgb "#888888" lt 1 lw 1.5
set grid back ls 11
set xlabel "year"
set ylabel "Population"
set output "../PNG/BrongAhafo.png"

plot "../Data/BrongAhafo_output.dat" using 1:2 title "." with points lt 7 lc 7 lw 2 dt 1, \
"../Data/BrongAhafo_output.dat" using 1:2 title "Actual Population" smooth csplines with lines lt 7 lc 7 lw 2, \
"../Data/BrongAhafo_output.dat" using 1:3 title "." with points lt 7 lc 9 lw 2 dt 1, \
"../Data/BrongAhafo_output.dat" using 1:3 title "Verhulst" smooth csplines with lines lt 7 lc 9 lw 2, \
"../Data/BrongAhafo_output.dat" using 1:4 title "." with points lt 7 lc 3 lw 2 dt 1, \
"../Data/BrongAhafo_output.dat" using 1:4 title "Gompertz" smooth csplines with lines lt 7 lc 3 lw 2,\
"../Data/BrongAhafo_output.dat" using 1:5 title "." with points lt 7 lc 5 lw 2 dt 1, \
"../Data/BrongAhafo_output.dat" using 1:5 title "Richards" smooth csplines with lines lt 7 lc 5 lw 2


set terminal pngcairo size 1200,800 font "Arial,12"
set title "Population growth of Northern Region,Ghana"
set grid
set style line 11 lc rgb "#888888" lt 1 lw 1.5
set grid back ls 11
set xlabel "year"
set ylabel "Population"
set output "../PNG/Northern.png"

plot "../Data/Northern_output.dat" using 1:2 title "." with points lt 7 lc 7 lw 2 dt 1, \
"../Data/Northern_output.dat" using 1:2 title "Actual Population" smooth csplines with lines lt 7 lc 7 lw 2, \
"../Data/Northern_output.dat" using 1:3 title "." with points lt 7 lc 9 lw 2 dt 1, \
"../Data/Northern_output.dat" using 1:3 title "Verhulst" smooth csplines with lines lt 7 lc 9 lw 2, \
"../Data/Northern_output.dat" using 1:4 title "." with points lt 7 lc 3 lw 2 dt 1, \
"../Data/Northern_output.dat" using 1:4 title "Gompertz" smooth csplines with lines lt 7 lc 3 lw 2,\
"../Data/Northern_output.dat" using 1:5 title "." with points lt 7 lc 5 lw 2 dt 1, \
"../Data/Northern_output.dat" using 1:5 title "Richards" smooth csplines with lines lt 7 lc 5 lw 2


set terminal pngcairo size 1200,800 font "Arial,12"
set title "Population growth of Upper East Region,Ghana"
set grid
set style line 11 lc rgb "#888888" lt 1 lw 1.5
set grid back ls 11
set xlabel "year"
set ylabel "Population"
set output "../PNG/UpperEast.png"

plot "../Data/UpperEast_output.dat" using 1:2 title "." with points lt 7 lc 7 lw 2 dt 1, \
"../Data/UpperEast_output.dat" using 1:2 title "Actual Population" smooth csplines with lines lt 7 lc 7 lw 2, \
"../Data/UpperEast_output.dat" using 1:3 title "." with points lt 7 lc 9 lw 2 dt 1, \
"../Data/UpperEast_output.dat" using 1:3 title "Verhulst" smooth csplines with lines lt 7 lc 9 lw 2, \
"../Data/UpperEast_output.dat" using 1:4 title "." with points lt 7 lc 3 lw 2 dt 1, \
"../Data/UpperEast_output.dat" using 1:4 title "Gompertz" smooth csplines with lines lt 7 lc 3 lw 2,\
"../Data/UpperEast_output.dat" using 1:5 title "." with points lt 7 lc 5 lw 2 dt 1, \
"../Data/UpperEast_output.dat" using 1:5 title "Richards" smooth csplines with lines lt 7 lc 5 lw 2


set terminal pngcairo size 1200,800 font "Arial,12"
set title "Population growth of Upper West Region,Ghana"
set grid
set style line 11 lc rgb "#888888" lt 1 lw 1.5
set grid back ls 11
set xlabel "year"
set ylabel "Population"
set output "../PNG/UpperWest.png"

plot "../Data/UpperWest_output.dat" using 1:2 title "." with points lt 7 lc 7 lw 2 dt 1, \
"../Data/UpperWest_output.dat" using 1:2 title "Actual Population" smooth csplines with lines lt 7 lc 7 lw 2, \
"../Data/UpperWest_output.dat" using 1:3 title "." with points lt 7 lc 9 lw 2 dt 1, \
"../Data/UpperWest_output.dat" using 1:3 title "Verhulst" smooth csplines with lines lt 7 lc 9 lw 2, \
"../Data/UpperWest_output.dat" using 1:4 title "." with points lt 7 lc 3 lw 2 dt 1, \
"../Data/UpperWest_output.dat" using 1:4 title "Gompertz" smooth csplines with lines lt 7 lc 3 lw 2,\
"../Data/UpperWest_output.dat" using 1:5 title "." with points lt 7 lc 5 lw 2 dt 1, \
"../Data/UpperWest_output.dat" using 1:5 title "Richards" smooth csplines with lines lt 7 lc 5 lw 2
