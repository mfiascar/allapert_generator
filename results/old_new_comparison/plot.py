import 	sys
sys.path.append("../../python_modules/")
from plot_allapert import plot

for number in range(1,9):
    ip = '%s'%number
    plot('LHCAperture_old.dat', 'LHCAperture_new.dat', 'x', ip, True)

for number in range(1,9):
    ip = '%s'%number
    plot('LHCAperture_old.dat','LHCAperture_new.dat', 'y', ip, True)
