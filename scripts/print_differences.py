import os,sys,string
from ROOT import *

def print_diff(file_1, file_2, reffile_1,  reffile_2, s_start=0., s_end=27000.):
    
    infile1 = open( file_1,"r")
    infile2 = open( file_2, "r")
    reffile = open( reffile_1, "r")
    reffile2 = open( reffile_2, "r")
    outfile =  open('differences_%s_to_%s.txt' %(s_start,s_end), 'w')
    outfile.write(' s \t name new  \t name old  \t diffx \t diffy \t diff(45) \n' )

    lines1 = infile1.readlines()
    lines2 = infile2.readlines()
    linesref = reffile.readlines()
    linesref2 = reffile2.readlines()
    count = -1
    countref = 0
    countref2 = 0

    ###############################################
    #First look at differences btw two aperture files
    ###############################################
    for l in lines1:
        count +=1
        if l.find("%")>=0:
            continue
        iline = l.split()
        s = float(iline[0])
        if s<s_start or s> s_end:
            #print "s %f outside ranges" %s
            continue
        x = float(iline[1])
        y = float(iline[2])
        d = float(iline[3])
        
        iline2 = lines2[count].split() 
        if float(iline[0])!= s:
            print "Error, s positions are different"
            continue
        diffx = float(iline2[1])- x
        diffy = float(iline2[2])- y
        diffd = float(iline2[3])- d
        if diffx!=0.0 or diffy!=0.0 or diffd!=0.0:
            #find closest marker
            min_diff = 9999999.
            e_name = ''
            min_diff_old = 9999999.
            e_name_old = ''
            
            #print "Found difference: %s" %s

            ################################################################################
            # If differences found, look for closest element in twiss file for new aperture
            ################################################################################
            for iref in range(countref,len(linesref)):
                if linesref[iref].find("@")>=0 or linesref[iref].find("*")>=0 or linesref[iref].find("%")>=0:
                    continue
                ilineref = linesref[iref].split()
                #ignore points with aperture = 0 
                if float(linesref[iref].split()[5])==0 and float(linesref[iref].split()[6])==0 and float(linesref[iref].split()[7])==0 and float(linesref[iref].split()[8])==0:
                    continue

                s_elem = float(ilineref[3])
                for iplus in range(1,5):
                    if (iref+iplus) <len(linesref):
                        s_elem_plus = float(linesref[iref+iplus].split()[3])
                        if s_elem_plus!=s_elem:
                            break
                    else:
                       s_elem_plus = s_elem
                       break
                            
                if fabs(s-s_elem) < min_diff:
                    min_diff = fabs(s-s_elem)
                    if fabs(s-s_elem_plus) >= fabs(s-s_elem):
                        e_name=ilineref[1]
                        countref = iref
                        break


            ################################################################################
            # Now look for closest element in twiss file for old aperture
            ################################################################################
            for iref in range(countref2,len(linesref2)):
                if linesref2[iref].find("@")>=0 or linesref2[iref].find("*")>=0 or linesref2[iref].find("%")>=0:
                    continue
                #ignore points with aperture = 0 
                if float(linesref2[iref].split()[5])==0 and float(linesref2[iref].split()[6])==0 and float(linesref2[iref].split()[7])==0 and float(linesref2[iref].split()[8])==0:
                    continue
                ilineref2 = linesref2[iref].split()

                s_elem = float(ilineref2[3])

                for iplus in range(1,5):
                    if (iref+iplus) <len(linesref2):
                        s_elem_plus = float(linesref2[iref+iplus].split()[3])
                        if s_elem_plus!=s_elem:
                            break
                    else:
                       s_elem_plus = s_elem
                       break
 
                if fabs(s-s_elem) < min_diff_old:
                    min_diff = fabs(s-s_elem)
                    if fabs(s-s_elem_plus) >= fabs(s-s_elem):
                        e_name_old=ilineref2[1]
                        countref2 = iref
                        break

            outfile.write(' %f \t %s \t  %s \t %f \t %f \t %f \n' %(s,e_name, e_name_old, diffx,diffy,diffd))

    infile1.close()
    infile2.close()
    outfile.close()
    reffile.close()
    reffile2.close()
            
#----------------------------------------------------------------------------#
#Example on how to use the function - print difference for selected s-range
#----------------------------------------------------------------------------#
print_diff('LHCAperture_new.dat','LHCAperture_old.dat','allapert_final.b1','allapert_roderik_for_maria.b1',0.,27000.)
