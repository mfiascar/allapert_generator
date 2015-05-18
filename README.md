# About this repository
This repository contains the tools used to generate a new aperture file, as input for [BeamLossPattern](https://lhc-collimation-project.web.cern.ch/lhc-collimation-project/BeamLossPattern.htm).

- [__bin__](https://github.com/KFubuki/allapert_generator/tree/master/bin): contains the executables.
- [__data__](https://github.com/KFubuki/allapert_generator/tree/master/data): contains a results folder, were the obtained results are organized by program that generated them. The input folder contains input files, organized by program that reads them. 
- [__doc__](https://github.com/KFubuki/allapert_generator/tree/master/doc): contains the documentation.
- [__fig__](https://github.com/KFubuki/allapert_generator/tree/master/fig): contains the figures.
- [__include__](https://github.com/KFubuki/allapert_generator/tree/master/include): contains the headers to compile BeamLossPattern or GetAperture.
- [__lib__](https://github.com/KFubuki/allapert_generator/tree/master/lib): contains the implementation files and the makefile to compile BeamLossPattern or GetAperture.
- [__scripts__](https://github.com/KFubuki/allapert_generator/tree/master/scripts): contains the data treatment and plotting Python scripts.


__Remark 1__: if you don't have access to AFS, you won't be able to use the files needed to run the MAD-X script.
__Remark 2__: to change the plotting parameters (limits, name of elements plotted, legends, name of file), change the [__plot_allapert.py__](https://github.com/KFubuki/allapert_generator/blob/master/scripts/plot_allapert.py) script in the [__scripts__](https://github.com/KFubuki/allapert_generator/tree/master/scripts) folder.
