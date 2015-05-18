echo ''
read -r -p '>> ATTENTION! The contents of the "data/results" folder will be wiped clean. Do you want to continue (y/n)? ' -n 1 -r
if [[ $REPLY =~ ^[Nn]$ ]]
then
    exit 0
fi

cd data/results/madx
rm *
cp ../../../scripts/*.madx .
madx < *.madx
rm *.madx

cd ../edit_twiss
rm *
cp ../madx/twiss_ip1_b1.tfs .
cp ../../../scripts/edit_twiss.py .
python edit_twiss.py
rm *.py
rm twiss_ip1_b1.tfs

cd ../GetAperture
cp ../edit_twiss/allapert_final.b1 .
ln -s ../../../bin/GetAperture
./GetAperture allapert_final.b1
mv LHCAperture.dat LHCAperture_new.dat
rm allapert_final.b1
cd ../../../

echo ''
read -r -p '>> Do you want to compare the latest LHCAperture.dat file generated with another file (y/n)? ' -n 1 -r
if [[ $REPLY =~ ^[Nn]$ ]]
then
    echo '>> The simulations end here. Exiting...'
    exit 0
fi

echo ''
cd data/input/GetAperture
ls -l

echo ''
read -r -p '>> Which one? > ' file

cp $file ../../results/GetAperture
cd ../../results/GetAperture
./GetAperture $file
mv LHCAperture.dat LHCAperture_old.dat
rm $file

cp LHC*  ../../../scripts
cp ../madx/twiss_ip1_b1.tfs  ../../../scripts
cd  ../../../scripts
python plot_allapert.py
mv *.png ../fig
rm LHC*
rm twiss_ip1_b1.tfs

echo '>> DONE!!'
