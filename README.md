# Code and supplementary material

Here you find the code and additional information for the paper "Two-sided markets from an agent-based modeling perspective" by Torsten Heinrich and Claudius Gräbner published in the International Journal of Computational Economics and Econometrics.

Detailed citation information: Heinrich, T. and Gräbner, C. (2017): Two-sided markets from an agent-based modeling perspective, in: *International Journal of Computational Economics and Econometrics*, forthcoming.


[Link to accepted working paper](https://ideas.repec.org/p/pra/mprapa/67860.html)

Link to the journal paper

In case you have questions of comments you may comment directly in the Github project or contact us directly via email.
Any feedback is highly appreciated!

## Abstract
Two-sided markets are an important aspect of today’s economies. 
Yet, the attention they have received in economic theory is limited, mainly due to methodological constraints of conventional approaches: 
Two-sided markets often exhibit non-trivial dynamics that are difficult to describe via analytical equilibrium models. 
We illustrate this point by revisiting a well-known equilibrium model of two-sided markets by Rochet and Tirole from an agent-based computational perspective. 
We identify several inconsistencies as well as implicit and implausible assumptions of the original model. 
These limit its explanatory power and motivate an alternative approach. 
The agent-based model we propose allows us to study two-sided markets in a more realistic and adequate manner: 
Not only are we able to compare different decision-making rules for the providers, we can also study situations with more than two providers. 
Thus, our model represents a first step towards a more realistic and policy-relevant study of two-sided markets.


## The agent-based model
You can obtain the code by cloning or downloading the associated repository via the link provided above.

Note that the main code is in the file `XXX.py`.

After having run the model, you can replicate the figures from the paper using the file `XXX.py`.

### Runing the model

We suggest to start the simulation using the associated callscript via a terminal using the following command:
```
./callscript.sh [<number of runs> [<start number> [<name string>]]]
```


You should have a folder called `output` and a folder called `figures` in the same directory as the source code.

You need to specify the kind of decision making algorithm used by the providers in the file `src-tms.py` directly (in lines 271-274 in the provider class).
The other relevant parameters that may be changed can be found in the beginning of the file.

In order to recreate the figures using the associated file "make_figure.py", we suggest to use the following name strings for the outputfiles:

`RIL_p01_[running_nb]` for the runs using reinforcement learning with 1 provider and without satisficing
`RIL_p10_[running_nb]` for the runs using reinforcement learning with 10 providers and without satisficing
`RILS_p01_[running_nb]` for the runs using reinforcement learning with 1 provider and with satisficing
`RILS_p10_[running_nb]` for the runs using reinforcement learning with 10 providers and with satisficing
`RO_p01_[running_nb]` for the runs using the rational optimization algorithm

The associated callscript puts running numbers automatically at the end of the outputfiles. So you call for example:
```
./callscript.sh 100 0 RIL_p01_
```
to obtain 100 runs of the simulation. The first result is then stored under the name `RIL_p01_00`, the last one
under the name `RIL_p01_99`.

You can find additional information for using the two scrips in the files themselves.
