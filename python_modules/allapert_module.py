import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

def plot_apertures(old, new, ip, coordinate):

    ip_name = '%s'%ip
    coord = '%s'%coordinate

    tup = []
    for line in open(old):
        value = line.strip("\n").split()
        tup.append(value)

    s = []
    x = []
    y = []
    for columns in tup: 
        s.append(float(columns[0]))
        x.append(float(columns[1]))
        y.append(float(columns[2]))

    tuples = []
    for line in open(new):
        value = line.strip("\n").split()
        tuples.append(value)

    s_new = []
    x_new = []
    y_new = []
    for column in tuples: 
        s_new.append(float(column[0]))
        x_new.append(float(column[1]))
        y_new.append(float(column[2]))

    t = (0, 3332.436584, 6664.7208, 9997.005016, 13329.28923, 16661.72582, 19994.1624, 23315.37898)
    length_acc = 26658.8832

    if ip == '1':
        position = t[0]
        zipped = zip(s, x, y)
        s_temp = []
        x_temp = []
        y_temp = []
        for e1, e2, e3 in zipped:
            if e1 < (length_acc / 2):
                s_temp.append(e1)
                x_temp.append(e2)
                y_temp.append(e3)
            if e1 >= (length_acc / 2):
                s_temp.append(e1 - length_acc)
                x_temp.append(e2)
                y_temp.append(e3)
        s_tot = []
        x_tot = []
        y_tot = []
        zipp = sorted(zip(s_temp, x_temp, y_temp), key = lambda t: t[0])
        for e1, e2, e3 in zipp:
            s_tot.append(e1)
            x_tot.append(e2)
            y_tot.append(e3)
        zipped_new = zip(s_new, x_new, y_new)
        s_temp_new = []
        x_temp_new = []
        y_temp_new = []
        for e1, e2, e3 in zipped_new:
            if e1 < (length_acc / 2):
                s_temp_new.append(e1)
                x_temp_new.append(e2)
                y_temp_new.append(e3)
            if e1 >= (length_acc / 2):
                s_temp_new.append(e1 - length_acc)
                x_temp_new.append(e2)
                y_temp_new.append(e3)
        s_tot_new = []
        x_tot_new = []
        y_tot_new = []
        zipp = sorted(zip(s_temp_new, x_temp_new, y_temp_new), key = lambda t: t[0])
        for e1, e2, e3 in zipp:
            s_tot_new.append(e1)
            x_tot_new.append(e2)
            y_tot_new.append(e3)
    elif ip == '2':
        position = t[1]
        s_tot = s
        x_tot = x
        y_tot = y
        s_tot_new = s_new
        x_tot_new = x_new
        y_tot_new = y_new
    elif ip == '3':
        position = t[2]
        s_tot = s
        x_tot = x
        y_tot = y
        s_tot_new = s_new
        x_tot_new = x_new
        y_tot_new = y_new
    elif ip == '4':
        position = t[3]
        s_tot = s
        x_tot = x
        y_tot = y
        s_tot_new = s_new
        x_tot_new = x_new
        y_tot_new = y_new
    elif ip == '5':
        position = t[4]
        s_tot = s
        x_tot = x
        y_tot = y
        s_tot_new = s_new
        x_tot_new = x_new
        y_tot_new = y_new
    elif ip == '6':
        position = t[5]
        s_tot = s
        x_tot = x
        y_tot = y
        s_tot_new = s_new
        x_tot_new = x_new
        y_tot_new = y_new
    elif ip == '7':
        position = t[6]
        s_tot = s
        x_tot = x
        y_tot = y
        s_tot_new = s_new
        x_tot_new = x_new
        y_tot_new = y_new
    elif ip == '8':
        position = t[7]
        s_tot = s
        x_tot = x
        y_tot = y
        s_tot_new = s_new
        x_tot_new = x_new
        y_tot_new = y_new
    else:
        print 'ERROR: input a number from 1 to 8 in 3rd argument of the function'

    if coord == 'x':
        var = x_tot
        var_new = x_tot_new
    elif coord == 'y':
        var = y_tot
        var_new = y_tot_new
    else:
        print 'ERROR: input coordinate x or y in 4th argument of the function'

    ax1.plot(s_tot, var, color = 'blue')
    ax1.set_xlim(position - 150, position + 150)
    ax1.set_ylim(0, 0.40)
    ax1.set_xlabel('s [m]')
    ax1.set_ylabel(coord + ' [m]')
    ax1.set_title('IP' + ip_name + ' (GetAperture in blue)')

    ax2.plot(s_tot_new, var_new, color = 'red')
    ax2.set_xlim(position - 150, position + 150)
    ax2.set_ylim(0, 0.40)
    ax2.set_xlabel('s [m]')
    ax2.set_ylabel(coord + ' [m]')

    pp = PdfPages('new_allapert_ip'+ ip_name + '_' + coord +'.pdf')
    pp.savefig()
    pp.close()




