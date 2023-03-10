#Program to get single raytrace of scales zemax in prism mode

DECLARE x,double,1,12100
DECLARE y,double,1,12100
DECLARE fx,double,1,5
DECLARE fy,double,1,5

SETCONFIG 3

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
SYSP 101, 5

SYSP 102, 1, x(z)
SYSP 103, 1, y(z)
SYSP 104, 1, 1

SYSP 102, 2, x(z)+2e-6
SYSP 103, 2, y(z)+2e-6
SYSP 104, 2, 1

SYSP 102, 3, x(z)-2e-6
SYSP 103, 3, y(z)+2e-6
SYSP 104, 3, 1

SYSP 102, 4, x(z)+2e-6
SYSP 103, 4, y(z)-2e-6
SYSP 104, 4, 1

SYSP 102, 5, x(z)-2e-6
SYSP 103, 5, y(z)-2e-6
SYSP 104, 5, 1

outputfile$="C:\Users\Admin\Documents\zemaxlogtracetotalM.txt"
SYSP 201, 1  # set total wavelength number as 1
filename$ = "C:\Users\Admin\Documents\scales_eoe_2022_multiwav\ls"
start_value =3.3#2.9000#1.95# 4.5000#1.95 #1.5965
stop_value = 2.45#4.1500#2.45# 5.2000#1.6783
increment = (stop_value-start_value)/4 #0.01

#start_value = 1.95 #1.5965
#stop_value =  2.45 #1.6783
#start_value = 2.2 #1.5965
#stop_value =  2.2 #1.6783
#increment = stop_value-start_value #0.01
format 6.8

FOR i, start_value, start_value, increment
   SYSP 202, 1, i
   SYSP 200, 1 # set the 2nd wavelength as the primary wavelength
   #A$ = $TEMPFILENAME()
   A$ = filename$ +"_"+$STR(z)+"_"+$STR(i) +".dat"
   GETTEXTFILE A$, Spt  
   OUTPUT outputfile$, APPEND
   ns=MAXF() 
   xminn=(x(z)-2e-6)/ns
   xmaxx=(x(z)+2e-6)/ns
   yminn=(y(z)-2e-6)/ns
   ymaxx=(y(z)+2e-6)/ns    
   xc=x(z)/ns
   yc=y(z)/ns
   
   fx(1)=xc
   fx(2)=xminn
   fx(3)=xminn
   fx(4)=xmaxx
   fx(5)=xmaxx

   fy(1)=yc
   fy(2)=yminn
   fy(3)=ymaxx
   fy(4)=yminn
   fy(5)=ymaxx
   
   FOR l,1,10,1
   FOR k,1,10,1
	xit=(xmaxx-xminn)/29
	yit=(ymaxx-yminn)/29
	xxx=xminn+(xit*l)
	yyy=yminn+(yit*k)
	xxx=xminn+(xmaxx-xminn)*RAND(1)
	yyy=yminn+(ymaxx-yminn)*RAND(1)
 	t=2*(22/7)*RAND(1)
 	r=RAND(1)
 	xp=r*COSI(t)
 	yp=r*SINE(t)
 	n = NSUR()

 	#RAYTRACE fx(l),fy(l),xp,yp,1
 	RAYTRACE xxx,yyy,xp,yp,1
 	xint = RAYX(n)
 	yint = RAYY(n)

 	PRINT xint," ",yint," ",x(z)," ",y(z)," ",ns," ",xxx," ",yyy," ",xminn," ",xmaxx," ",yminn," ",ymaxx," ",xp," ",yp
	
	next k
	next l

   
NEXT i


#PRINT z
NEXT z



