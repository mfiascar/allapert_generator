import sys
sys.path.append("../python_modules")
from allapert_module import plot_apertures

for number in range(1,8):
    ip = '%s'%number
    plot_apertures('../get_aperture/LHCAperture.dat', '../data_treatment/plot_allapert.txt', ip, 'x')

# for number in range(1,8):
#     ip = '%s'%number
#     plot_apertures('../get_aperture/LHCAperture.dat', '../data_treatment/plot_allapert.txt', ip, 'y')
    

