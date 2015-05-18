read -r -p '>> ATTENTION! The contents of the "data" folder will be wiped clean. Do you want to continue (y/n)? ' -n 1 -r
if [[ $REPLY =~ ^[Nn]$ ]]
then
    exit 0
fi

echo ''

rm data/*

cp scripts/*.madx data
cp scripts/edit_allapert.py data
cd data
echo '>> This are the files for your simulation'
ls -l

cd data
madx < *.madx
python edit_allapert.py

ls -lt

ln -s ../bin/GetAperture
./GetAperture allapert_final.b1

mv LHCAperture.dat LHCAperture_new.dat

ls -lt

echo ''
read -r -p '>> Do you want to compare LHCAperture.dat with another file (y/n)? ' -n 1 -r
if [[ $REPLY =~ ^[Nn]$ ]]
then
    exit 0
fi

echo ''
cd ../allapert_files
ls -l
cd ../data

echo ''
read -r -p '>> Which one? > ' file

cp ../allapert_files/$file .

./GetAperture $file

ls -l

mv LHCAperture.dat LHCAperture_old.dat

cp LHC* ../scripts
cp twiss_ip1_b1.tfs ../scripts
cd ../scripts
python plot_allapert.py
mv *.png ../fig
rm LHC*
rm twiss_ip1_b1.tfs
rm *.png

echo '>> DONE!!'
