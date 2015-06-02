# -------------------------------------------------
# Script to compare different allapert files
# -------------------------------------------------
import re
import sys
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams
from util import *

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
        var_x, var_y = get_columns(file_1, 0, 1)
        var_x2, var_y2 = get_columns(file_2, 0, 1)
        ax.set_ylabel('x [m]')

    elif coord =='y':
        var_x, var_y = get_columns(file_1, 0, 2)
        var_x2, var_y2 = get_columns(file_2, 0, 2)
        ax.set_ylabel('y [m]')

    else:
        print '>> ERROR: input "x" or "y" in the 3rd argument'

    # ---------------
    # Choose the s range
    # ---------------
    s_range = [-1.,-1.]
    y_range = [0.,0.03]
    title = ""
    try:
        int(ip)
        print "Going to plot IP %i, coord %s" %(ip,coord) 

        y_limits = (0.2, 0.65, 0.2, 0.2, 0.4, 0.2, 0.2, 0.3)
        position, ylim = get_ir(ip, y_limits[ip-1])
        s_range = [position - 150, position + 150]
        y_range = [0, ylim]
        title = 'IR%i' %ip

        if ip == 1:
            var_x, var_y = get_ip1(var_x, var_y)
            var_x2, var_y2 = get_ip1(var_x2, var_y2)

        # -------------------------------------
        # Choose the elements you want to plot
        # -------------------------------------
        regex_list = (['VC+', 'T'], ['VC+'], ['VC+'], ['VC+'], ['VC+', 'T'], ['VC+'], ['VC+'], ['VC+'])
        heights = (0.12, 0.42, 0.1, 0.13, 0.23, 0.1, 0.1, 0.2)

        name, pos, height = get_element('twiss_ip1_b1.tfs', 0, 3, regex_list[ip-1], heights[ip-1])

        if flag == True:
        # ------------------
        # Plot the elements
        # ------------------
            if ip == 1:
                pos, name = get_ip1(pos, name)
            for s, n in zip(pos, name):
                plt.annotate(n, xy=(s, height), xytext=(s, height), name='Verdana', family='sans-serif', 
                             weight='light', va='bottom', ha='center', rotation=90, size=3)
                    # plt.bar(s-l, 100, l, 150, color = '#249A27', edgecolor = 'black', linewidth = '1.7', alpha = 0.
        else:
            print 'No elements were plotted'

    except ValueError:
        
        s_range = get_range('twiss_ip1_b1.tfs',"S."+ip,"E."+ip)
        title = ip
        print "Going to plot from S.%s at s=%f to E.%s s=%f, coord %s" %(ip, s_range[0], ip, s_range[1], coord)

    # ---------
    # Plotting
    # ---------
    ax.plot(var_x, var_y, 'b-', linewidth=1, label='Old file')
    ax.plot(var_x2, var_y2, 'r-', linewidth=0.4, label='New file')
    ip = '%s'%ip
    ax.set_title(title)
    ax.set_xlim(s_range)
    ax.set_ylim(y_range)
    ax.set_xlabel('s [m]')
    ax.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
    ax.grid(b=None, which='major')
    ax.legend(loc='upper right', prop={'size':6})
    plt.subplots_adjust(left=0.12,bottom=0.16,right=0.94,top=0.88)
    # plt.show()
    
    # --------------
    # Save the plot
    # --------------
    plt.savefig('allapert_' + title + '_' + coord + '_new.png', dpi=DPI)
    plt.close()
    

# -----------------
# Use the function
# -----------------
coords = ['x','y']
el_name = [ "DS.R1.B1",
            "DS.R2.B1",
            "DS.R3.B1",
            "DS.R4.B1",
            "DS.R5.B1",
            "DS.R6.B1",
            "DS.R7.B1",
            "DS.R8.B1",
            "DS.L1.B1",
            "DS.L2.B1",
            "DS.L3.B1",
            "DS.L4.B1",
            "DS.L5.B1",
            "DS.L6.B1",
            "DS.L7.B1",
            "DS.L8.B1",
            "ARC.12.B1",
            "ARC.23.B1",
            "ARC.34.B1",
            "ARC.45.B1",
            "ARC.56.B1",
            "ARC.67.B1",
            "ARC.78.B1"]
for c in coords:
    for number in range(1,9):
        plot('LHCAperture_old.dat', 'LHCAperture_new.dat', c, number, True)
    for e in el_name:
        plot('LHCAperture_old.dat', 'LHCAperture_new.dat', c, e, False)
 
