# allapert_generator
This repository contains the tools used to generate a new aperture file, as input for [BeamLossPattern](https://lhc-collimation-project.web.cern.ch/lhc-collimation-project/BeamLossPattern.htm).

1. Create a folder in [__input__](https://github.com/KFubuki/allapert_generator/tree/master/input/old_new_comparison) with:
..* MAD-X file
..* Old allapert file processed by GetAperture
..* Plotting script (can be found in [__data_treatment__](https://github.com/KFubuki/allapert_generator/tree/master/data_treatment))

2. Execute the [__run.sh__](https://github.com/KFubuki/allapert_generator/blob/master/run.sh) script
3. Check the results folder to see the plots

__Remarks__: to change the plotting parameters (limits, name of elements plotted, legends, name of file), change the [__plot_allapert.py__](https://github.com/KFubuki/allapert_generator/blob/master/python_modules/plot_allapert.py) script in the [__python_modules__](https://github.com/KFubuki/allapert_generator/tree/master/python_modules) folder.
