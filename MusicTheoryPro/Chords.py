"""Code for creating all the Chords in form of Html tags"""
notes=["A ","A#","B ","C ","C#","D ","D#","E ","F ","F#","G ","G#"]

majformula=[4,3]
minformula=[3,4]

ofile=open("Chords.txt",'w')
ofile.write("MAJOR CHORDS\n")
for scale in range(len(notes)):
            ofile.write("</tr>\n")
            ofile.write("<tr>\n")
            ofile.write("<td>"+notes[scale]+"</td>"+'\n')
            majind=0
            num=scale
            i=1
            while i<=3:
                        i=i+1
                        ofile.write("<td>"+notes[num]+"</td>"+'\n')
                        num=num+majformula[majind]
                        majind=majind+1
                        if (majind>=2):
                                    majind=majind-2
                        if(num>=12):
                                    num=num-12
ofile.write("</tr>\n")
ofile.close()

ofile=open("Chords.txt",'a')
ofile.write("MINOR CHORDS\n")
for scale in range(len(notes)):
            ofile.write("</tr>\n")
            ofile.write("<tr>\n")
            ofile.write("<td>"+notes[scale]+"</td>"+'\n')
            minind=0
            num=scale
            i=1
            while i<=3:
                        i=i+1
                        ofile.write("<td>"+notes[num]+"</td>"+'\n')
                        num=num+minformula[minind]
                        minind=minind+1
                        if (minind>=2):
                                    minind=minind-2
                        if(num>=12):
                                    num=num-12
ofile.write("</tr>\n")
ofile.close()

