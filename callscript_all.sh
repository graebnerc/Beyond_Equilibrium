#!/bin/bash
# bash call script for tsm simulations; hands the python program the filename with a running id number as string of constant length
#
#  1. USAGE
# to be called like so (from same working directory that contains the python program):
#					./callscript.sh
#
#  2. TROUBLESHOOTING
# In case of error "bash: ./callscript.sh: Permission denied" add permission to execute like so:
#					chmod +x callscript.sh
#

# functions
makeleadingzeros() {	# accepts arguments: (string) (number of leading zeros)
    # function manipulates strings to introduce leading zeros; used to ensure identical filename length
    local sI=$1
    local vlength=$2
    for (( j=0; j<vlength-1; j+=1 )); 	# don't use i; would interfere with loop below
      do
        sI='0'$sI						# add sufficiently many or more leading zeros
    done
    sI=${sI:( -vlength)}				# retain only the last (vlength) digits
    echo $sI							# return value
}

# default values
vstart=0								# first id; typically 0
vend=201								# last id
vlength=${#vend}						# string length of last id

# main entry point
#main entry point
for nbuyers in 125 250 500 1000 2000 4000 8000 16000 32000;	#main loop for different runs for different numbers of buyers
  do
    vlengthNB=5							#maximum (160000) has len 6
    outputfilename=bs_RO_p01_ef0_$(makeleadingzeros $nbuyers $vlengthNB)	#obtain constant length id number for file name from makeleadingzeros() function above
    python tsm-src-3.py strategy=RO providernum=1 nbuyers=$nbuyers tmax=151 filename=$outputfilename	#script call
done
# RIL, 10 providers
for (( i=$vstart; i<$vend; i+=1 )); 	# main loop for different runs
  do
    sI=$(makeleadingzeros $i $vlength)	# obtain constant length id number for file name from makeleadingzeros() function above
    python tsm-src-3.py strategy=RIL providernum=10 runid=$sI	# script call
done
# RIL, 1 provider 
for (( i=$vstart; i<$vend; i+=1 )); 	# main loop for different runs
  do
    sI=$(makeleadingzeros $i $vlength)	# obtain constant length id number for file name from makeleadingzeros() function above
    python tsm-src-3.py strategy=RIL providernum=1 runid=$sI	# script call
done
# RILS, 1 provider 
for (( i=$vstart; i<$vend; i+=1 )); 	# main loop for different runs
  do
    sI=$(makeleadingzeros $i $vlength)	# obtain constant length id number for file name from makeleadingzeros() function above
    python tsm-src-3.py strategy=RILS providernum=1 runid=$sI	# script call
done
# RILS, 10 providers
for (( i=$vstart; i<$vend; i+=1 )); 	# main loop for different runs
  do
    sI=$(makeleadingzeros $i $vlength)	# obtain constant length id number for file name from makeleadingzeros() function above
    python tsm-src-3.py strategy=RILS providernum=10 runid=$sI	# script call
done
# R0, 1 provider, fixed entry fee 0
vend=101	#only 100 runs for RO simulations as they take considerably longer
for (( i=$vstart; i<$vend; i+=1 )); 	# main loop for different runs
  do
    sI=$(makeleadingzeros $i $vlength)	# obtain constant length id number for file name from makeleadingzeros() function above
    python tsm-src-3.py strategy=RO providernum=1 fixedentryfee=0 runid=$sI	# script call
done
# RO, 10 providers, fixed entry fee -200
for (( i=$vstart; i<$vend; i+=1 )); 	# main loop for different runs
  do
    sI=$(makeleadingzeros $i $vlength)	# obtain constant length id number for file name from makeleadingzeros() function above
    python tsm-src-3.py strategy=RO providernum=1 fixedentryfee=-200 runid=$sI	# script call
done
# RILS, 10 providers, per customer fixed cost 0 
vend=201	#200 runs for all RIL simulations
for (( i=$vstart; i<$vend; i+=1 )); 	# main loop for different runs
  do
    sI=$(makeleadingzeros $i $vlength)	# obtain constant length id number for file name from makeleadingzeros() function above
    python tsm-src-3.py strategy=RILS providernum=10 pcc=0 runid=$sI	# script call
done
# RILS, 10 providers, per customer fixed cost 50
for (( i=$vstart; i<$vend; i+=1 )); 	# main loop for different runs
  do
    sI=$(makeleadingzeros $i $vlength)	# obtain constant length id number for file name from makeleadingzeros() function above
    python tsm-src-3.py strategy=RILS providernum=10 pcc=10 runid=$sI	# script call
done

# create figures. Note that this will not work with python3
python2 figures_paper_colored.py
python2 figures_paper_greyscale.py
exit 0
