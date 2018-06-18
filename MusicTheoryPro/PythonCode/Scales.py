"""Code for creating all the Chords in form of Html tags"""
notes=["A ","A#","B ","C ","C#","D ","D#","E ","F ","F#","G ","G#"]

majformula=[2,2,1,2,2,2,1]
minformula=[2,1,2,2,1,2,2]

ofile=open("Chords.txt",'w')
ofile.write("MAJOR SCALES\n")
for scale in range(len(notes)):
            ofile.write("</tr>\n")
            ofile.write("<tr>\n")
            ofile.write("<td>"+notes[scale]+"</td>"+'\n')
            majind=0
            num=scale
            i=1
            while i<=8:
                        i=i+1
                        ofile.write("<td>"+notes[num]+"</td>"+'\n')
                        num=num+majformula[majind]
                        majind=majind+1
                        if (majind>=7):
                                    majind=majind-7
                        if(num>=12):
                                    num=num-12
ofile.write("</tr>\n")
ofile.close()

ofile=open("Chords.txt",'a')
ofile.write("MINOR SCALES\n")
for scale in range(len(notes)):
            ofile.write("</tr>\n")
            ofile.write("<tr>\n")
            ofile.write("<td>"+notes[scale]+"</td>"+'\n')
            minind=0
            num=scale
            i=1
            while i<=8:
                        i=i+1
                        ofile.write("<td>"+notes[num]+"</td>"+'\n')
                        num=num+minformula[majind]
                        minind=minind+1
                        if (minind>=7):
                                    minind=minind-7
                        if(num>=12):
                                    num=num-12
ofile.write("</tr>\n")
ofile.close()

