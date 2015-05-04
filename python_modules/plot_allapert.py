# -------------------------------------------------
# Script to compare different allapert files
# -------------------------------------------------
import re
import sys
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams
from plotting_tools import get_columns
from plotting_tools import get_element
from plotting_tools import get_ip1
from plotting_tools import get_ir

def plot(file_1, file_2, coord, ip, flag): # Here, file_1 is thought as the output of the GetAperture routine and file_2 a MAD-X file 

    # -----------------------------
    # Text and plot characteristics
    # -----------------------------
    DPI = 300
    textwidth = 4
    rc('font',**{'family':'serif','serif':['Computer Modern Roman'], 'size':10})
    rc('text', usetex=True)
    rcParams['figure.figsize']=textwidth, textwidth/1.618

    fig = plt.figure()
    ax = fig.add_subplot(111)

    coord = '%s'%coord

    # -----------------------------
    # Deal with each possible case
    # -----------------------------
    # --------------------------------
    # Get the data for each coordinate
    # --------------------------------
    if coord =='x':
        var_x, var_y = get_columns('LHCAperture_old.dat', 0, 1)
        var_x2, var_y2 = get_columns('LHCAperture_new.dat', 0, 1)
        ax.set_ylabel('x [m]')

    elif coord =='y':
        var_x, var_y = get_columns('LHCAperture_old.dat', 0, 2)
        var_x2, var_y2 = get_columns('LHCAperture_new.dat', 0, 2)
        ax.set_ylabel('y [m]')

    else:
        print '>> ERROR: input "x" or "y" in the 3rd argument'

    # ---------------
    # Choose your IR 
    # ---------------
    y_limits = (0.2, 0.6, 0.23, 0.23, 0.4, 0.23, 0.23, 0.3)
    position, ylim = get_ir(ip, y_limits[ip-1])

    if ip == 1:
        var_x, var_y = get_ip1(var_x, var_y)
        var_x2, var_y2 = get_ip1(var_x2, var_y2)

    # -------------------------------------
    # Choose the elements you want to plot
    # -------------------------------------
    regex_list = (['VC+', 'T'], ['VC+'], ['VC+'], ['VC+'], ['VC+', 'T'], ['VC+'], ['VC+'], ['VC+'])

    name, pos, height = get_element('twiss_ip1_b1.tfs', 0, 3, regex_list[ip-1], y_limits[ip-1]-0.05)

    if flag == True:
    # ------------------
    # Plot the elements
    # ------------------
        for s, n in zip(pos, name):
            plt.annotate(n, xy=(s, height), xytext=(s, height), name='Verdana', family='sans-serif', 
                         weight='light', va='bottom', ha='center', rotation=90, size=3)
                # plt.bar(s-l, 100, l, 150, color = '#249A27', edgecolor = 'black', linewidth = '1.7', alpha = 0.
    else:
        print 'No elements were plotted'

    # ---------
    # Plotting
    # ---------
    ax.plot(var_x, var_y, 'b-', linewidth=1, label='Old file')
    ax.plot(var_x2, var_y2, 'r-', linewidth=0.4, label='New file')
    ip = '%s'%ip
    ax.set_title('IR' + ip)
    ax.set_xlim([position - 150, position + 150])
    ax.set_ylim([0, ylim])
    ax.set_xlabel('s [m]')
    ax.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
    ax.grid(b=None, which='major')
    ax.legend(loc='upper right', prop={'size':6})
    plt.subplots_adjust(left=0.12,bottom=0.16,right=0.94,top=0.88)
    # plt.show()
    
    # --------------
    # Save the plot
    # --------------
    plt.savefig('allapert_ip_' + ip + '_' + coord + '_new.png', dpi=DPI)
    plt.close()

