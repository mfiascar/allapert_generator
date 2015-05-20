import os,sys,string
import glob


infile1 = open("twiss_ip1_b1_markersToAdd.tfs", 'r')
infile2 = open("twiss_ip1_b1.tfs", 'r') #twiss_ip1_b1.tfs
outfile =  open('twiss_ip1_b1_withNewMarkers.tfs', 'w')
iline1 = infile1.readlines()
iline = infile2.readlines()
s_pos = []
count = 0
for item1 in iline1:
    s_pos += [float(item1.split()[3])]
    
for item in iline:
    if item[0] == '@' or item[0] == '$' or item[0] == '*':
        outfile.write(item)
        continue
    columns = item.split()
    s = float(columns[3])
    if count<len(s_pos) and s_pos[count]<s:
        outfile.write(iline1[count])
        count +=1
    outfile.write(item)
        
print "Wrote out: %i new markers (%i)" %(count,len(s_pos))
print "Line of file twiss_ip1_b1_markersToAdd.tfs: %i" %len(iline1)

