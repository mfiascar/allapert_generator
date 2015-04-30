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
from plotting_tools import get_ip1
from plotting_tools import get_ir
from plotting_tools import get_element


def plot(file_1, file_2, coord, ip, name): # Here, file_1 is thought as the output of the GetAperture routine and file_2 a MAD-X file 

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

    ip = '%s'%ip
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

    # ------------------------------------------------------------------------------
    # Define the text height, elements to be printed and vertical limit for each IR
    # ------------------------------------------------------------------------------
    if ip == '1':
        position, height, regex_list, ylim = get_ir(1, 0.13, "['VC+', 'T']", 0.25)
        var_x, var_y = get_ip1(var_x, var_y)
        var_x2, var_y2 = get_ip1(var_x2, var_y2)

    elif ip == '2':
        position, height, regex_list, ylim = get_ir(2, 0.43, "['VC+']", 0.6)

    elif ip == '3':
        position, height, regex_list, ylim = get_ir('3', 0.9, "['VC+']", 0.2)

    elif ip == '4':
        position, height, regex_list, ylim = get_ir('4', 0.13, "['VC+']", 0.23)

    elif ip == '5':
        position, height, regex_list, ylim = get_ir('5', 0.23, "['VC+', 'T']", 0.4)

    elif ip == '6':
        position, height, regex_list, ylim = get_ir('6', 0.1, "['VC+']", 0.2)

    elif ip == '7':
        position, height, regex_list, ylim = get_ir('7', 0.1, "['VC+']", 0.2)

    elif ip == '8':
        position, height, regex_list, ylim = get_ir('8', 0.2, "['VC+']", 0.3)

    else:
        print '>> ERROR: input a number from 1 to 8 in the 4th argument'

    # ------------------
    # Plot the elements
    # ------------------
    # if name==True:
    #     n = []
    #     p = []
    #     with open('twiss_ip1_b1.tfs', 'r') as infile:
    #         for character in infile:
    #             columns = character.strip().split()
    #             n.append(columns[0].strip('"'))
    #             p.append(columns[3])

    #     name = []
    #     pos = []
    #     for a in regex_list:
    #         regex = re.compile(a)
    #         for a, b in zip(n,p):
    #             if regex.match(a):
    #                 name.append(a)
    #                 pos.append(b)
    pos, name = get_element('twiss_ip1_b1.tfs', regex_list, name, 0, 3)

    for s, element in zip(pos, name):
        f = s
        plt.annotate(element, xy=(f, height), xytext=(s, height), name='Verdana', family='sans-serif', 
                     weight='light', va='bottom', ha='center', rotation=90, size=3)
            # plt.bar(s-l, 100, l, 150, color = '#249A27', edgecolor = 'black', linewidth = '1.7', alpha = 0.3)
    #     print '>> Element names were written for IP%s, coord. %s' %(ip, coord) 
    # elif name==False:
    #     print '>> No element names were written for IP%s,coord. %s' %(ip, coord)
    # else:
    #     print '>> Enter "True" or "False" in the last argument of the function please!' 

    # ---------
    # Plotting
    # ---------
    ax.plot(var_x, var_y, 'b-', linewidth=1, label='Old file')
    ax.plot(var_x2, var_y2, 'r-', linewidth=0.4, label='New file')
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

