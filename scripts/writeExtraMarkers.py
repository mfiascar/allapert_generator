import os,sys,string
import glob

infile = open("twiss_ip1_b1_thick.tfs","r")
outfile =  open('twiss_ip1_b1_markersToAdd.tfs', 'w')
iline = infile.readlines()
for item in iline:
    if item[0] == '@' or item[0] == '$' or item[0] == '*':
        continue
    columns = item.split()
    #ignore elements with no lenght
    if float(columns[4])==0:
        continue
    #ignore elements with no aperture
    if ( float(columns[5])==0 and float(columns[6])==0 and float(columns[7])==0 and float(columns[8])==0):
        continue
    s = float(columns[3])
    L = float(columns[4])
    s_start = s -L
    s_end = s
    outfile.write(' %s \t %s \t %s \t %f \t %f \t %f \t %f \t %f \t %f \n' % (columns[0], columns[1], columns[2], s_start, 0.0, float(columns[5]), float(columns[6]), float(columns[7]), float(columns[8])))
    outfile.write(' %s \t %s \t %s \t %f \t %f \t %f \t %f \t %f \t %f \n' % (columns[0], columns[1], columns[2], s_end, 0.0, float(columns[5]), float(columns[6]), float(columns[7]), float(columns[8])))
outfile.close()
infile.close()

