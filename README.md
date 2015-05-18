# About this repository
This repository contains the tools used to generate a new aperture file, as input for [BeamLossPattern](https://lhc-collimation-project.web.cern.ch/lhc-collimation-project/BeamLossPattern.htm).

- [__allapert_files__](https://github.com/KFubuki/allapert_generator/tree/master/allapert_files): contains the old allapert files.
- [__bin__](https://github.com/KFubuki/allapert_generator/tree/master/bin): contains the executables.
- [__data__](https://github.com/KFubuki/allapert_generator/tree/master/data): contains the MAD-X script generating the new allapert file and data used for the analysis (read only).
- [__doc__](https://github.com/KFubuki/allapert_generator/tree/master/doc): contains the documentation.
- [__fig__](https://github.com/KFubuki/allapert_generator/tree/master/fig): contains the figures.
- [__include__](https://github.com/KFubuki/allapert_generator/tree/master/include): contains the headers to compile BeamLossPattern or GetAperture.
- [__lib__](https://github.com/KFubuki/allapert_generator/tree/master/lib): contains the implementation files and the makefile to compile BeamLossPattern or GetAperture.
- [__scripts__](https://github.com/KFubuki/allapert_generator/tree/master/scripts): contains the data treatment and plotting Python scripts.


## How it works

1. Place your MAD-X script to generate the new allapert file in [__data__](https://github.com/KFubuki/allapert_generator/tree/master/data).

2. Execute the [__run.sh__](https://github.com/KFubuki/allapert_generator/blob/master/run.sh) script and follow the instructions.

3. Check the [__fig__](https://github.com/KFubuki/allapert_generator/tree/master/fig) folder to see the plots.

__Remarks__: to change the plotting parameters (limits, name of elements plotted, legends, name of file), change the [__plot_allapert.py__](https://github.com/KFubuki/allapert_generator/blob/master/scripts/plot_allapert.py) script in the [__scripts__](https://github.com/KFubuki/allapert_generator/tree/master/scripts) folder.
