set xrange [0:10]
set yrange [-5:10]
unset key
set arrow 1 from 0,0 to 10,0 nohead
set arrow 2 from 0,-5 to 0,10 nohead
#set arrow 3 from 6.5,-5 to 6.5,-1 nohead ls 3 lc 8
#set arrow 4 from 6.5,0 to 6.5,10 nohead ls 3 lc 8
#set label 1 at 6.15,-.5 's_{max}-a^i'
#set label 2 at 9,-.5 's_{max}'
set ylabel 'D^i=s(n^{j*}),  n_i'
set xlabel 'D^j=s(n^{i*}), n^j'
set term postscr color enhanced 'Helvetica' 20
set output "gnuplot-fig-04.ps"
plot 9-2.5-3/x ls 1 lw 3 lc 3, 6.5<x ? 1/0: 3/(9-2.5-x) ls 1 lw 1 lc 3
#ps2pdf gnuplot-fig-04.ps
