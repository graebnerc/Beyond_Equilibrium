set xrange [0:10]
set yrange [-5:10]
unset key
set arrow 1 from 0,0 to 10,0 nohead
set arrow 2 from 0,-5 to 0,10 nohead
set arrow 3 from 2.5,-5 to 2.5,-1 nohead ls 3 lc 8
set arrow 4 from 2.5,0 to 2.5,10 nohead ls 3 lc 8
set label 1 at 2.45,-.5 'a^i'
#set label 2 at -1.2,-3 'B^i-A^i'
set xlabel 'b^i'
set ylabel 'n^j^*(b^i)'
set term postscr color enhanced 'Helvetica' 20
set output "gnuplot-fig-02.ps"
plot 3/(x-2.5) ls 1 lw 3 lc 3
#plot x>0 ? -3+x : 1/0 ls 1 lw 3 lc 3
#ps2pdf gnuplot-fig-02.ps
