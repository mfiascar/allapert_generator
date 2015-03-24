# Execute MAD-X script
cd madx_generator
madx < generate_allapert.madx

# Edit the generated file (delete 0 and 9.999 apertures, delete collimators)
cd ../data_treatment
python allapert_editor.py
sed --in-place '/\"TC/d' allapert_final.b1
cp allapert_final.b1 ../get_aperture

# Execute GetAperture
cd ../get_aperture
./GetAperture allapert_final.b1
perl -pi -e 's/\0/  /g' LHCAperture.dat
sed -i '/^%/d' LHCAperture.dat

# Plot the comparison
cd ../plots
python plot.py 
