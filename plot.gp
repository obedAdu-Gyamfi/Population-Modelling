#!/usr/bin/env gnuplot

set terminal pngcairo size 1200,800 font "Arial,12"
set title "Population growth of Western Region,Ghana"
set grid
set style line 11 lc rgb "#888888" lt 1 lw 1.5
set grid back ls 11
set xlabel "year"
set ylabel "Population"
set output "./PNG/Western.png"

plot "./output/Western_output.dat" using 1:2 title "." with points lt 7 lc 7 lw 2 dt 1, \
"./output/Western_output.dat" using 1:2 title "Actual Population" smooth csplines with lines lt 7 lc 7 lw 2, \
"./output/Western_output.dat" using 1:3 title "." with points lt 7 lc 9 lw 2 dt 1, \
"./output/Western_output.dat" using 1:3 title "Verhulst" smooth csplines with lines lt 7 lc 9 lw 2, \
"./output/Western_output.dat" using 1:4 title "." with points lt 7 lc 3 lw 2 dt 1, \
"./output/Western_output.dat" using 1:4 title "Gompertz" smooth csplines with lines lt 7 lc 3 lw 2,\
"./output/Western_output.dat" using 1:5 title "." with points lt 7 lc 5 lw 2 dt 1, \
"./output/Western_output.dat" using 1:5 title "Richards" smooth csplines with lines lt 7 lc 5 lw 2

set terminal pngcairo size 1200,800 font "Arial,12"
set title "Population growth of Central Region,Ghana"
set grid
set style line 11 lc rgb "#888888" lt 1 lw 1.5
set grid back ls 11
set xlabel "year"
set ylabel "Population"
set output "./PNG/Central.png"

plot "./output/Central_output.dat" using 1:2 title "." with points lt 7 lc 7 lw 2 dt 1, \
"./output/Central_output.dat" using 1:2 title "Actual Population" smooth csplines with lines lt 7 lc 7 lw 2, \
"./output/Central_output.dat" using 1:3 title "." with points lt 7 lc 9 lw 2 dt 1, \
"./output/Central_output.dat" using 1:3 title "Verhulst" smooth csplines with lines lt 7 lc 9 lw 2, \
"./output/Central_output.dat" using 1:4 title "." with points lt 7 lc 3 lw 2 dt 1, \
"./output/Central_output.dat" using 1:4 title "Gompertz" smooth csplines with lines lt 7 lc 3 lw 2,\
"./output/Central_output.dat" using 1:5 title "." with points lt 7 lc 5 lw 2 dt 1, \
"./output/Central_output.dat" using 1:5 title "Richards" smooth csplines with lines lt 7 lc 5 lw 2


set terminal pngcairo size 1200,800 font "Arial,12"
set title "Population growth of Greater Accra Region,Ghana"
set grid
set style line 11 lc rgb "#888888" lt 1 lw 1.5
set grid back ls 11
set xlabel "year"
set ylabel "Population"
set output "./PNG/GreaterAccra.png"

plot "./output/GreaterAccra_output.dat" using 1:2 title "." with points lt 7 lc 7 lw 2 dt 1, \
"./output/GreaterAccra_output.dat" using 1:2 title "Actual Population" smooth csplines with lines lt 7 lc 7 lw 2, \
"./output/GreaterAccra_output.dat" using 1:3 title "." with points lt 7 lc 9 lw 2 dt 1, \
"./output/GreaterAccra_output.dat" using 1:3 title "Verhulst" smooth csplines with lines lt 7 lc 9 lw 2, \
"./output/GreaterAccra_output.dat" using 1:4 title "." with points lt 7 lc 3 lw 2 dt 1, \
"./output/GreaterAccra_output.dat" using 1:4 title "Gompertz" smooth csplines with lines lt 7 lc 3 lw 2,\
"./output/GreaterAccra_output.dat" using 1:5 title "." with points lt 7 lc 5 lw 2 dt 1, \
"./output/GreaterAccra_output.dat" using 1:5 title "Richards" smooth csplines with lines lt 7 lc 5 lw 2

set terminal pngcairo size 1200,800 font "Arial,12"
set title "Population growth of Volta Region,Ghana"
set grid
set style line 11 lc rgb "#888888" lt 1 lw 1.5
set grid back ls 11
set xlabel "year"
set ylabel "Population"
set output "./PNG/Volta.png"

plot "./output/Volta_output.dat" using 1:2 title "." with points lt 7 lc 7 lw 2 dt 1, \
"./output/Volta_output.dat" using 1:2 title "Actual Population" smooth csplines with lines lt 7 lc 7 lw 2, \
"./output/Volta_output.dat" using 1:3 title "." with points lt 7 lc 9 lw 2 dt 1, \
"./output/Volta_output.dat" using 1:3 title "Verhulst" smooth csplines with lines lt 7 lc 9 lw 2, \
"./output/Volta_output.dat" using 1:4 title "." with points lt 7 lc 3 lw 2 dt 1, \
"./output/Volta_output.dat" using 1:4 title "Gompertz" smooth csplines with lines lt 7 lc 3 lw 2,\
"./output/Volta_output.dat" using 1:5 title "." with points lt 7 lc 5 lw 2 dt 1, \
"./output/Volta_output.dat" using 1:5 title "Richards" smooth csplines with lines lt 7 lc 5 lw 2

set terminal pngcairo size 1200,800 font "Arial,12"
set title "Population growth of Eastern Region,Ghana"
set grid
set style line 11 lc rgb "#888888" lt 1 lw 1.5
set grid back ls 11
set xlabel "year"
set ylabel "Population"
set output "./PNG/Eastern.png"

plot "./output/Eastern_output.dat" using 1:2 title "." with points lt 7 lc 7 lw 2 dt 1, \
"./output/Eastern_output.dat" using 1:2 title "Actual Population" smooth csplines with lines lt 7 lc 7 lw 2, \
"./output/Eastern_output.dat" using 1:3 title "." with points lt 7 lc 9 lw 2 dt 1, \
"./output/Eastern_output.dat" using 1:3 title "Verhulst" smooth csplines with lines lt 7 lc 9 lw 2, \
"./output/Eastern_output.dat" using 1:4 title "." with points lt 7 lc 3 lw 2 dt 1, \
"./output/Eastern_output.dat" using 1:4 title "Gompertz" smooth csplines with lines lt 7 lc 3 lw 2,\
"./output/Eastern_output.dat" using 1:5 title "." with points lt 7 lc 5 lw 2 dt 1, \
"./output/Eastern_output.dat" using 1:5 title "Richards" smooth csplines with lines lt 7 lc 5 lw 2


set terminal pngcairo size 1200,800 font "Arial,12"
set title "Population growth of Ashanti Region,Ghana"
set grid
set style line 11 lc rgb "#888888" lt 1 lw 1.5
set grid back ls 11
set xlabel "year"
set ylabel "Population"
set output "./PNG/Ashanti.png"

plot "./output/Ashanti_output.dat" using 1:2 title "." with points lt 7 lc 7 lw 2 dt 1, \
"./output/Ashanti_output.dat" using 1:2 title "Actual Population" smooth csplines with lines lt 7 lc 7 lw 2, \
"./output/Ashanti_output.dat" using 1:3 title "." with points lt 7 lc 9 lw 2 dt 1, \
"./output/Ashanti_output.dat" using 1:3 title "Verhulst" smooth csplines with lines lt 7 lc 9 lw 2, \
"./output/Ashanti_output.dat" using 1:4 title "." with points lt 7 lc 3 lw 2 dt 1, \
"./output/Ashanti_output.dat" using 1:4 title "Gompertz" smooth csplines with lines lt 7 lc 3 lw 2,\
"./output/Ashanti_output.dat" using 1:5 title "." with points lt 7 lc 5 lw 2 dt 1, \
"./output/Ashanti_output.dat" using 1:5 title "Richards" smooth csplines with lines lt 7 lc 5 lw 2


set terminal pngcairo size 1200,800 font "Arial,12"
set title "Population growth of Brong Ahafo Region,Ghana"
set grid
set style line 11 lc rgb "#888888" lt 1 lw 1.5
set grid back ls 11
set xlabel "year"
set ylabel "Population"
set output "./PNG/BrongAhafo.png"

plot "./output/BrongAhafo_output.dat" using 1:2 title "." with points lt 7 lc 7 lw 2 dt 1, \
"./output/BrongAhafo_output.dat" using 1:2 title "Actual Population" smooth csplines with lines lt 7 lc 7 lw 2, \
"./output/BrongAhafo_output.dat" using 1:3 title "." with points lt 7 lc 9 lw 2 dt 1, \
"./output/BrongAhafo_output.dat" using 1:3 title "Verhulst" smooth csplines with lines lt 7 lc 9 lw 2, \
"./output/BrongAhafo_output.dat" using 1:4 title "." with points lt 7 lc 3 lw 2 dt 1, \
"./output/BrongAhafo_output.dat" using 1:4 title "Gompertz" smooth csplines with lines lt 7 lc 3 lw 2,\
"./output/BrongAhafo_output.dat" using 1:5 title "." with points lt 7 lc 5 lw 2 dt 1, \
"./output/BrongAhafo_output.dat" using 1:5 title "Richards" smooth csplines with lines lt 7 lc 5 lw 2


set terminal pngcairo size 1200,800 font "Arial,12"
set title "Population growth of Northern Region,Ghana"
set grid
set style line 11 lc rgb "#888888" lt 1 lw 1.5
set grid back ls 11
set xlabel "year"
set ylabel "Population"
set output "./PNG/Northern.png"

plot "./output/Northern_output.dat" using 1:2 title "." with points lt 7 lc 7 lw 2 dt 1, \
"./output/Northern_output.dat" using 1:2 title "Actual Population" smooth csplines with lines lt 7 lc 7 lw 2, \
"./output/Northern_output.dat" using 1:3 title "." with points lt 7 lc 9 lw 2 dt 1, \
"./output/Northern_output.dat" using 1:3 title "Verhulst" smooth csplines with lines lt 7 lc 9 lw 2, \
"./output/Northern_output.dat" using 1:4 title "." with points lt 7 lc 3 lw 2 dt 1, \
"./output/Northern_output.dat" using 1:4 title "Gompertz" smooth csplines with lines lt 7 lc 3 lw 2,\
"./output/Northern_output.dat" using 1:5 title "." with points lt 7 lc 5 lw 2 dt 1, \
"./output/Northern_output.dat" using 1:5 title "Richards" smooth csplines with lines lt 7 lc 5 lw 2


set terminal pngcairo size 1200,800 font "Arial,12"
set title "Population growth of Upper East Region,Ghana"
set grid
set style line 11 lc rgb "#888888" lt 1 lw 1.5
set grid back ls 11
set xlabel "year"
set ylabel "Population"
set output "./PNG/UpperEast.png"

plot "./output/UpperEast_output.dat" using 1:2 title "." with points lt 7 lc 7 lw 2 dt 1, \
"./output/UpperEast_output.dat" using 1:2 title "Actual Population" smooth csplines with lines lt 7 lc 7 lw 2, \
"./output/UpperEast_output.dat" using 1:3 title "." with points lt 7 lc 9 lw 2 dt 1, \
"./output/UpperEast_output.dat" using 1:3 title "Verhulst" smooth csplines with lines lt 7 lc 9 lw 2, \
"./output/UpperEast_output.dat" using 1:4 title "." with points lt 7 lc 3 lw 2 dt 1, \
"./output/UpperEast_output.dat" using 1:4 title "Gompertz" smooth csplines with lines lt 7 lc 3 lw 2,\
"./output/UpperEast_output.dat" using 1:5 title "." with points lt 7 lc 5 lw 2 dt 1, \
"./output/UpperEast_output.dat" using 1:5 title "Richards" smooth csplines with lines lt 7 lc 5 lw 2


set terminal pngcairo size 1200,800 font "Arial,12"
set title "Population growth of Upper West Region,Ghana"
set grid
set style line 11 lc rgb "#888888" lt 1 lw 1.5
set grid back ls 11
set xlabel "year"
set ylabel "Population"
set output "./PNG/UpperWest.png"

plot "./output/UpperWest_output.dat" using 1:2 title "." with points lt 7 lc 7 lw 2 dt 1, \
"./output/UpperWest_output.dat" using 1:2 title "Actual Population" smooth csplines with lines lt 7 lc 7 lw 2, \
"./output/UpperWest_output.dat" using 1:3 title "." with points lt 7 lc 9 lw 2 dt 1, \
"./output/UpperWest_output.dat" using 1:3 title "Verhulst" smooth csplines with lines lt 7 lc 9 lw 2, \
"./output/UpperWest_output.dat" using 1:4 title "." with points lt 7 lc 3 lw 2 dt 1, \
"./output/UpperWest_output.dat" using 1:4 title "Gompertz" smooth csplines with lines lt 7 lc 3 lw 2,\
"./output/UpperWest_output.dat" using 1:5 title "." with points lt 7 lc 5 lw 2 dt 1, \
"./output/UpperWest_output.dat" using 1:5 title "Richards" smooth csplines with lines lt 7 lc 5 lw 2
