cd input
ls -ld */
cd ..
read -r -p 'Select input folder from the list above >>> ' folder
mkdir -p results
if [ -d results/$folder ]; then
  sudo rm -r results/$folder
fi
mkdir results/$folder
cp input/$folder/* results/$folder
cd results/$folder
ls -l

cp ../../data_treatment/allapert_editor.py .
cp ../../executables/GetAperture .

# Execute MAD-X script
echo '>> Executing MAD-X'
madx < generate_allapert.madx

# Treat the file to make it work with GetAperture
echo '>> Treating the Twiss file'
python allapert_editor.py

# Execute GetAperture and clean the file
echo '>> Executing GetAperture'
./GetAperture allapert_*.b1
perl -pi -e 's/\0/  /g' LHCAperture.dat
sed -i '/^%/d' LHCAperture.dat

# Rename the output created for the new aperture file 
mv LHCAperture.dat LHCAperture_new.dat

# Plot the comparison
echo '>> Plotting'
python plot_allapert.py 

echo '>> DONE!!'
