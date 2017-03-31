set xrange [-2:10]
set yrange [-5:10]
unset key
set arrow 1 from -2,0 to 10,0 nohead
set arrow 2 from 0,-5 to 0,10 nohead
set arrow 201 from 0,-3 to 0,10 nohead ls 1 lw 3 lc 3
set arrow 31 from .75,4 to 0,0
set arrow 32 from 1.5,2.5 to 1.5,0
set arrow 33 from 3,1 to 3,0
set arrow 34 from 5,3 to 6,0
set label 11 at .25,4.7 'n^{j*}(b_1^i)'
set label 12 at 1.,3.2 'n^{j*}(b_2^i)'
set label 13 at 2.5,1.5 'n^{j*}(b_3^i)'
set label 14 at 4.5,3.7 'n^{j*}(b_4^i)'
set label 2 at -1.2,-3 'B^i-A^i'
set label 31 at 0.2,8.5 'b_1^i={/Symbol \245}'
set label 32 at 5,8.5 'b_2^i'
set label 33 at 8,6 'b_3^i'
set label 34 at 8,2 'b_4^i'
set label 35 at 8,-2.3 'b_5^i=a^i'
set label 36 at 2,-4.35 'b_6^i<a^i'
set xlabel 'n^j'
set ylabel 'U^i'
set term postscr color enhanced 'Helvetica' 20
set output "gnuplot-fig-00.ps"
plot x>0 ? -3+x : 1/0 ls 1 lw 3 lc 3, x>0 ? -3+2*x : 1/0 ls 1 lw 3 lc 3,x>0 ? -3+0.5*x : 1/0 ls 1 lw 3 lc 3,x>0 ? -3 : 1/0 ls 1 lw 3 lc 3,x>0 ? -3-0.2*x : 1/0 ls 1 lw 3 lc 3
#ps2pdf gnuplot-fig-00.ps
