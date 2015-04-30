# -------------------------------------------------
# Script to compare different allapert files
# -------------------------------------------------
import re
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams

# Color options
#--------------
# D   = '#419AD9'        # Dipoles: MBX, MBXW, MBRC, MBRS, MBW, MBRB
# Q1  = '#249A27'        # MQXA
# Q2  = '#55E058'        # MQXB
# M   = '#EEBE4C'        # Kickers & Correctors: MC, MK
# B   = '#9342AE'        # Beam Instrumentation: B
# V   = '#A1AAA2'        # Vacuum elements
# TC  = '#EE634C'        # Collimators
# TAN = '#8C3C2F'        # TAN & TAS
# spec='#9342AE'       # Spectrometers & compensators: MBAW, MBLW, MBWMD, MBXWH

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

    # --------------------
    # Position of each IP
    # --------------------
    t = (0, 3332.436584, 6664.7208, 9997.005016, 13329.28923, 16661.72582, 19994.1624, 23315.37898)
    length_acc = 26658.8832
    
    # ------------------------------
    # Functions to extract the data
    # ------------------------------
    def get_data():
        for line in open(file_1):
            columns = line.strip('\n').split()
            if columns[0] == '#':
                continue
            yield columns

    # -----------------------------
    # Deal with each possible case
    # -----------------------------
    # ------------
    # Coordinates
    # ------------
    if coord =='x':
        def get_coord():
            var_x = []
            var_y = []
            data = get_data()
            for column in data:
                var_x.append(float(column[0]))
                var_y.append(float(column[1]))
            return var_x, var_y
        var_x, var_y = get_coord()

        var_x2 = []
        var_y2 = []
        for line in open(file_2):
            columns_2 = line.strip('\n').split()
            var_x2.append(float(columns_2[0]))
            var_y2.append(float(columns_2[1]))

        ax.set_ylabel('x [m]')

    elif coord =='y':
        def get_coord():
            var_x = []
            var_y = []
            data = get_data()
            for column in data:
                var_x.append(float(column[0]))
                var_y.append(float(column[2]))
            return var_x, var_y
        var_x, var_y = get_coord()

        var_x2 = []
        var_y2 = []
        for line in open(file_2):
            columns_2 = line.strip('\n').split()
            var_x2.append(float(columns_2[0]))
            var_y2.append(float(columns_2[3]))

        ax.set_ylabel('y [m]')

    else:
        print '>> ERROR: input "x" or "y" in the 3rd argument'

    # ---
    # IP
    # ---
    if ip == '1':
        position = t[0]
        zipped = zip(var_x, var_y)
        x_temp = []
        y_temp = []
        for e1, e2 in zipped:
            if e1 < (length_acc / 2):
                x_temp.append(e1)
                y_temp.append(e2)
            if e1 >= (length_acc / 2):
                x_temp.append(e1 - length_acc)
                y_temp.append(e2)

        sort = sorted(zip(x_temp, y_temp), key=lambda t: t[0])
        x = []
        y = []
        for e1, e2 in sort:
            x.append(e1)
            y.append(e2)

        zipped2 = zip(var_x2, var_y2)
        x_temp2 = []
        y_temp2 = []
        for e1, e2 in zipped2:
            if e1 < (length_acc / 2):
                x_temp2.append(e1)
                y_temp2.append(e2)
            if e1 >= (length_acc / 2):
                x_temp2.append(e1 - length_acc)
                y_temp2.append(e2)

        sort2 = sorted(zip(x_temp2, y_temp2), key=lambda t: t[0])
        x2 = []
        y2 = []
        for e1, e2 in sort:
            x2.append(e1)
            y2.append(e2)

        height = 0.13
        regex_list = ['VC+', 'T']
        ylim = 0.25

    elif ip == '2':
        position = t[1]
        x = var_x
        y = var_y
        x2 = var_x2
        y2 = var_y2
        height = 0.43
        regex_list = ['VC+']
        ylim = 0.6

    elif ip == '3':
        position = t[2]
        x = var_x
        y = var_y
        x2 = var_x2
        y2 = var_y2
        ax.set_ylim([0, 0.2])
        height = 0.9
        regex_list = ['M+']
        ylim = 0.2

    elif ip == '4':
        position = t[3]
        x = var_x
        y = var_y
        x2 = var_x2
        y2 = var_y2
        ax.set_ylim([0, 0.2])
        height = 0.13
        regex_list = ['VC+']
        ylim = 0.23

    elif ip == '5':
        position = t[4]
        x = var_x
        y = var_y
        x2 = var_x2
        y2 = var_y2
        height = 0.23
        regex_list = ['VC+', 'T']
        ylim = 0.4

    elif ip == '6':
        position = t[5]
        x = var_x
        y = var_y
        x2 = var_x2
        y2 = var_y2
        height = 0.1
        regex_list = ['VC+']
        ylim = 0.2

    elif ip == '7':
        position = t[6]
        x = var_x
        y = var_y
        x2 = var_x2
        y2 = var_y2
        height = 0.1
        regex_list = ['VC+']
        ylim = 0.2

    elif ip == '8':
        position = t[7]
        x = var_x
        y = var_y
        x2 = var_x2
        y2 = var_y2
        height = 0.2
        regex_list = ['VC+']
        ylim = 0.3

    else:
        print '>> ERROR: input a number from 1 to 8 in the 4th argument'

    # ------------------
    # Plot the elements
    # ------------------
    if name==True:
        n = []
        p = []
        with open('twiss_ip1_b1.tfs', 'r') as infile:
            for character in infile:
                columns = character.strip().split()
                n.append(columns[0].strip('"'))
                p.append(columns[3])

        name = []
        pos = []
        for a in regex_list:
            regex = re.compile(a)
            for a, b in zip(n,p):
                if regex.match(a):
                    name.append(a)
                    pos.append(b)

        for s, element in zip(pos, name):
            f = s
            plt.annotate(element, xy=(f, height), xytext=(s, height), name='Verdana', family='sans-serif', 
                         weight='light', va='bottom', ha='center', rotation=90, size=3)
            # plt.bar(s-l, 100, l, 150, color = '#249A27', edgecolor = 'black', linewidth = '1.7', alpha = 0.3)
        print '>> Element names were written for IP%s, coord. %s' %(ip, coord) 
    elif name==False:
        print '>> No element names were written for IP%s,coord. %s' %(ip, coord)
    else:
        print '>> Enter "True" or "False" in the last argument of the function please!' 

    # ---------
    # Plotting
    # ---------
    ax.plot(x, y, 'b-', linewidth=1, label='Old file')
    ax.plot(x2, y2, 'r-', linewidth=0.4, label='New file')
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

