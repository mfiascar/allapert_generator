import re

with open('../madx_generator/allapert_twiss.b1', 'r') as infile:
    with open('allapert_final.b1', 'w') as outfile:
        line = infile.readlines()
        for item in line:
            if item[0] == '@' or item[0] == '$' or item[0] == '*':
                outfile.write(item)
    outfile.close()
infile.close()

with open('../madx_generator/allapert_twiss.b1', 'r') as infile:
    with open('allapert_final.b1', 'a') as outfile:
        for character in infile:
            columns = character.strip().split()
            if character[0] != '@' and character[0] != '$' and character[0] != '*':
                if float(columns[5]) != 0 and float(columns[6]) == 0:
                    outfile.write('%20s %-17s %19s %23f %18f %15f %18f %18f %18f \n' % (columns[0], columns[1], columns[2], float(columns[3]), float(columns[4]), float(columns[5]), float(columns[5]), float(columns[7]), float(columns[8])))
                elif float(columns[5]) == 0 and float(columns[6]) != 0:
                    outfile.write('%20s %-17s %19s %23f %18f %15f %18f %18f %18f \n' % (columns[0], columns[1], columns[2], float(columns[3]), float(columns[4]), float(columns[6]), float(columns[6]), float(columns[7]), float(columns[8])))

                elif float(columns[5]) != 0 and float(columns[6]) != 0 and float(columns[7]) != 0 and float(columns[8]) != 0 and float(columns[5]) != 9.999999 and float(columns[6]) != 9.999999 and float(columns[7]) != 9.999999 and float(columns[8]) != 9.999999:
                    outfile.write('%20s %-17s %19s %23f %18f %15f %18f %18f %18f \n' % (columns[0], columns[1], columns[2], float(columns[3]), float(columns[4]), float(columns[5]), float(columns[6]), float(columns[7]), float(columns[8])))
                # else:
                #     outfile.write('%20s %-17s %19s %23f %18f %15f %18f %18f %18f \n' % (columns[0], columns[1], columns[2], float(columns[3]), float(columns[4]), float(columns[5]), float(columns[6]), float(columns[7]), float(columns[8])))

    outfile.close()
infile.close()

with open('allapert_final.b1', 'r') as infile:
    with open('plot_allapert.txt', 'w') as outfile:
        for character in infile:
            columns = character.strip().split()
            if character[0] != '@' and character[0] != '$' and character[0] != '*':
                outfile.write('%0s %15f %15f %15f %15f \n' % (columns[3], float(columns[5]), float(columns[6]), float(columns[7]), float(columns[8])))
    outfile.close()
infile.close()
