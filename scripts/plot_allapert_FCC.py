# ----------------------------------------------------------------
# Script to plot the aperture, given the output of GetAperture
# ----------------------------------------------------------------
import re
import sys
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams
from util import *

def plot(file_1, twissfile, coord, ip, flag): # Here, file_1 is thought as the output of the GetAperture routine and file_2 a MAD-X file 

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
        ax.set_ylabel('x [m]')

    elif coord =='y':
        var_x, var_y = get_columns(file_1, 0, 2)
        ax.set_ylabel('y [m]')

    else:
        print '>> ERROR: input "x" or "y" in the 3rd argument'

    # ---------------
    # Choose the s range
    # ---------------
    s_range = [-1.,-1.]
    y_range = [0.,0.045]
    title = ""
    
    #name of ips
    ips = [ "A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L" ]
    #s-pos of ips
    ips_s = [ 1087.717331 , -1., -1., -1., -1., -1., 49744.998465, -1., -1., -1., -1., -1. ]

    try:
        int(ip)
        my_ip = "IP%s" %ips[ip-1]
        print "Going to plot %s, coord %s" %(my_ip,coord) 

        #y_limits = (0.2, 0.65, 0.2, 0.2, 0.4, 0.2, 0.2, 0.3)
        position = ips_s[ip-1]
        if position < 0:
            print "Error, IP not defined"
        s_range = [position - 550, position + 550]
        y_range = [0, 0.1]
        title = my_ip

        #yet to be fixed
        #if ip == 1:
        #    zipped = zip(var_x, var_y)
        #    x_temp = []
        #    y_temp = []
        #    for e1, e2 in zipped:
        #        if e1 < (97314.56227 / 2):
        #            x_temp.append(e1)
        #            y_temp.append(e2)
        #        if e1 >= (97314.56227 / 2):
        #            x_temp.append(e1 - 97314.56227)
        #            y_temp.append(e2)
        #    x = []
        #    y = []
        #    for e1, e2 in sorted(zip(x_temp, y_temp), key=lambda t: t[0]):
        #        x.append(e1)
        #        y.append(e2)
        #    var_x = x
        #    var_y = y

        # -------------------------------------
        # Choose the elements you want to plot
        # -------------------------------------
        regex_list = (['VC+', 'T'], ['VC+'], ['VC+'], ['VC+'], ['VC+', 'T'], ['VC+'], ['VC+'], ['VC+'])
        heights = (0.12, 0.42, 0.1, 0.13, 0.23, 0.1, 0.1, 0.2)

        name, pos, height = get_element(twissfile, 0, 3, regex_list[ip-1], heights[ip-1])

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
        
        s_range = get_range(twissfile,"S."+ip,"E."+ip)
        title = ip
        print "Going to plot from S.%s at s=%f to E.%s s=%f, coord %s" %(ip, s_range[0], ip, s_range[1], coord)

    # ---------
    # Plotting
    # ---------
    ax.plot(var_x, var_y, 'b-', linewidth=1, label='')
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
    plt.savefig('allapert_' + title + '_' + coord + '.png', dpi=DPI)
    plt.close()
    

# -----------------
# Use the function
# -----------------
coords = ['x','y']
el_name = [ "DS.RA.H1",
            "DS.LB.H1",
            "DS.RB.H1",
            "DS.LD.H1",
            "DS.RD.H1",
            "DS.LF.H1",
            "DS.RF.H1",
            "DS.LG.H1",
            "DS.RG.H1",
            "DS.LH.H1",
            "DS.RH.H1",
            "DS.LJ.H1",
            "DS.RJ.H1",
            "DS.LL.H1",
            "DS.RL.H1",
            "DS.LA.H1",
            "CELL.AB.H1",
            "CELL.BC.H1",
            "CELL.CD.H1",
            "CELL.DE.H1",
            "CELL.EF.H1",
            "CELL.FG.H1",
            "CELL.GH.H1",
            "CELL.HI.H1",
            "CELL.IJ.H1",
            "CELL.JK.H1",
            "CELL.KL.H1",
            "CELL.LA.H1",
            "COLL_D",
            "COLL_J"]
for c in coords:
    plot('FCCAperture.b1.dat', 'twiss_aperture_thick_b1.tfs', c, 1, False)
    plot('FCCAperture.b1.dat', 'twiss_aperture_thick_b1.tfs', c, 7, False)
    for e in el_name:
        plot('FCCAperture.b1.dat', 'twiss_aperture_thick_b1.tfs', c, e, False)
 
