# --------------------------------------------
# Series of useful functions to help plotting
# --------------------------------------------
import re

def get_lines(infile):
    """Extracts the lines of a data file. Used in the get_columns function."""
    for character in open(infile):
        columns = character.strip('\n').split()
        if columns[0] == '#' or columns[0] == '@' or columns[0] == '*' or columns[0] == '$' or columns[0] == '%':
            continue
        yield columns

def get_columns(infile, x, y):
    """Extracts the columns of a data file using the get_lines function. 

    The function arguments' are (in order): 
    - File
    - Number of the column corresponding to coordinate x
    - Number of the column corresponding to coordinate y

    Example:
    var_x, var_y = get_columns('LHCAperture_old.dat', 0, 2)
    """
    var_x = []
    var_y = []
    my_data = get_lines(infile)
    for column in my_data:
        var_x.append(float(column[x]))
        var_y.append(float(column[y]))
    return var_x, var_y

def get_ip1(x,y):
    """Treats the x and y coordinates already extracted from the data in order to easily plot
    around IP1 (i.e. convert s coordinate of 26900 m to -100 m).

    The function arguments' are the variables x and y that you want to treat, respectively . 

    Example:
    var_x, var_y = get_ip1(var_x, var_y)
    """
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

def get_ir(ir, ylim):
    """This function stores the information relevant to the plotting of a specific Interaction Region (IR), 
    i.e. the position of the IR in the accelerator and the limit of the vertical coordinate.

    The function arguments' are (in order):
    - Number of the IR (from 1 to 8, both included)
    - Limit in the vertical coordinate

    Example:
    position, ylim = get_ir(2, 0.6)
    """
    t = (0, 3332.436584, 6664.7208, 9997.005016, 13329.28923, 16661.72582, 19994.1624, 23315.37898)
    position = t[ir-1]
    return position, ylim

def get_element(infile, column_name, column_position, regex, text_height):
    """This function extracts the information relevant to the plotting of the accelerator's elements.

    The function arguments' are (in order):
    - File 
    - Number of the column corresponding to the name
    - Number of the column corresponding to the position
    - List of regular expressions defining the elements you want to plot (e.g. all that start with the 
    letter 'V')
    - The height at which the name of the element will appear in the plot

    Example:
    name, pos, height = get_element('twiss_ip1_b1.tfs', 0, 3, ['VC+'], 0.6)
    """
    name = []
    position = []
    my_data = get_lines(infile)
    for column in my_data:
        name.append(column[column_name].strip('"'))
        position.append(float(column[column_position]))

    new_name = []
    new_position = []
    for expression in regex:
        regex = re.compile(expression)
        for e1, e2 in zip(name,position):
            if regex.match(e1):
                new_name.append(e1)
                new_position.append(e2)
    return new_name, new_position, text_height

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
# spec= '#9342AE'       # Spectrometers & compensators: MBAW, MBLW, MBWMD, MBXWH
