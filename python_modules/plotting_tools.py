# -------------------------------------------------
# Series of very useful functions to help plotting
# -------------------------------------------------
import re

# Function to extract lines from a file
def get_lines(infile):
    for character in open(infile):
        columns = character.strip('\n').split()
        if columns[0] == '#':
            continue
        yield columns

# Function to extract columns from a file
def get_columns(infile, x, y):
    var_x = []
    var_y = []
    my_data = get_lines(infile)
    for column in my_data:
        var_x.append(float(column[x]))
        var_y.append(float(column[y]))
    return var_x, var_y

# Function to treat the data starting from IP1
def get_ip1(x,y):
    zipped = zip(x, y)
    x_temp = []
    y_temp = []
    for e1, e2 in zipped:
        if e1 < (26658.8832 / 2):
            x_temp.append(e1)
            y_temp.append(e2)
        if e1 >= (26658.8832 / 2):
            x_temp.append(e1 - 26658.8832)
            y_temp.append(e2)
    x = []
    y = []
    for e1, e2 in sorted(zip(x_temp, y_temp), key=lambda t: t[0]):
        x.append(e1)
        y.append(e2)
    return x,y

# Function to plot different IR's with different characteristics
def get_ir(ip, text_height, element_regex, ylim):
    t = (0, 3332.436584, 6664.7208, 9997.005016, 13329.28923, 16661.72582, 19994.1624, 23315.37898)
    position = t[ip-1]
    return position, text_height, element_regex, ylim

# Function to annotate the element's names
def get_element(infile, regex, flag, column_name, column_position):
    if flag==True:
        name = []
        position = []
        with open(infile, 'r') as infile:
            for character in infile:
                columns = character.strip().split()
                name.append(columns[column_name].strip('"'))
                position.append(columns[column_position])

        new_name = []
        new_position = []
        for expression in regex:
            regex = re.compile(expression)
            for e1, e2 in zip(name,position):
                if regex.match(expression):
                    new_name.append(e1)
                    new_position.append(e2)
        return new_name, new_position

    #     print '>> Element names were written for IP%s, coord. %s' %(ip, coord) 
    # elif flag==False:
    #     print '>> No element names were written for IP%s,coord. %s' %(ip, coord)
    # else:
    #     print '>> Enter "True" or "False" in the last argument of the function please!' 

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
