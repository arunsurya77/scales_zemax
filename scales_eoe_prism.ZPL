#AA$ = "C:\Users\Arun\Documents\ka.txt"
#GETTEXTFILE AA$, POP    # Import POP text data file
DECLARE x,double,1,12100
DECLARE y,double,1,12100
SETCONFIG 4

filename$ = "C:\Users\Admin\Documents\x_scaleseoe_new.txt"#xfullarr_new_eoe.txt
OPEN filename$
FOR z,1,12100,1
READNEXT x1
x(z)=x1#*3.174603e-6
#PRINT x(z)
NEXT z
CLOSE

filename$ = "C:\Users\Admin\Documents\y_scaleseoe_new.txt"
OPEN filename$
#SETCONFIG z
FOR z,1,12100,1
READNEXT y1
y(z)=y1#*3.174603e-6
#PRINT y(z)
NEXT z
CLOSE


PRINT "Hello"
FOR z,1,12100,1

SYSP 100, 0
SYSP 101, 1

SYSP 102, 1, x(z)
SYSP 103, 1, y(z)
SYSP 104, 1, 1


outputfile$="C:\Users\aruns\Documents\lenslet\ZN3.txt"
SYSP 201, 1  # set total wavelength number as 1
filename$ = "C:\Users\Admin\Documents\scales_eoe_final\Kband_prism\ls"
start_value =1.95#2.9000#1.95# 4.5000#1.95 #1.5965
stop_value = 2.45#4.1500#2.45# 5.2000#1.6783
increment = (stop_value-start_value)/4 #0.01

#start_value = 1.95 #1.5965
#stop_value =  2.45 #1.6783
#start_value = 2.2 #1.5965
#stop_value =  2.2 #1.6783
#increment = stop_value-start_value #0.01
FOR i, start_value, stop_value, increment
   SYSP 202, 1, i
   SYSP 200, 1 # set the 2nd wavelength as the primary wavelength
   #A$ = $TEMPFILENAME()
   A$ = filename$ +"_"+$STR(z)+"_"+$STR(i) +".dat"
   GETTEXTFILE A$, Spt   
   
NEXT i
PRINT z
NEXT z



