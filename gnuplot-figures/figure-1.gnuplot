set xrange [-2:10]
set yrange [-0.1:0.5]
unset key
set arrow 1 from -2,0 to 10,0 nohead ls 1 lc 0
set arrow 2 from 0,-.1 to 0,.5 nohead ls 1 lc 0
set label 1 at 2.15,-.05 'a^i=s_{min}'
set label 2 at 8.75,-.05 's_{max}'
set xlabel 'b^i'
set ylabel 'PDF'
set term postscr color enhanced 'Helvetica' 20
set output "gnuplot-fig-01.ps"
plot x<2.5 ? 0: x<9 ? 1/7.5 : 0 ls 1 lw 3 lc 3
#ps2pdf gnuplot-fig-01.ps
