import numpy as np
import matplotlib.pyplot as plt
import math

for ind in range(5,6,1):	
	prism_index=ind
	x_index=np.loadtxt('x_index.txt')
	y_index=np.loadtxt('y_index.txt')
	prism_title_arr=['R80','R140','R250','R60','R35','R200']
	prism_titleband_arr=['L-band','M-band','CH4/PAH','water ice','SEDs','K-band']
	prism_title=prism_title_arr[prism_index]
	prism_title_plot=prism_titleband_arr[prism_index]
	def ismissing(x,y):
	   if np.logical_and(np.logical_and(x<1024,x>-1024),np.logical_and(y<1024,y>-1024)):
	       return 0
	   else:
	       return 1
	
	xx=[]
	yy=[]
	arr=[]
	fig = plt.figure(1)
	ax = fig.add_subplot(111)
	ax.set_xlim([-25,25])
	ax.set_ylim([-25,25])
	count_in=0
	count_out=0
	
	
	#wave_samp=np.arange(1.9600,2.0604,.002)
	wave_samp_arr=[]
	wave_samp_arr.append(np.linspace(2.9000,4.1500,5))#LBand
	wave_samp_arr.append(np.linspace(4.5000,5.2000,5))#Mband
	wave_samp_arr.append(np.linspace(3.1000,3.5000,5))#R250
	wave_samp_arr.append(np.linspace(2.0000,3.7000,5))#R60
	wave_samp_arr.append(np.linspace(2.0001,5.0001,5))#R35
	wave_samp_arr.append(np.linspace(1.9500,2.4500,5))#R200
	wave_samp=wave_samp_arr[prism_index]
	
	xlis=np.zeros([5,12100])
	ylis=np.zeros([5,12100])
	xlis_field=np.zeros([5,12100])
	ylis_field=np.zeros([5,12100])
	miss_flag=np.zeros([110,110])
	cnt=0
	for j in wave_samp:
	        arr_x=[]
	        arr_y=[]
	        arr_x_field=[]
	        arr_y_field=[]
	        for i in range(1,12101,1): #
	                arr=[]
	                wave='{:01.4f}'.format(j)
	
	                filename= 'scales_eoe_final/Kband_prism/ls_'+str(i)+'.0000_'+wave+'.dat'
	                print(filename)
	                with open(filename) as f:
	                        for line in f:
	                                result=line.split()
	                                if len(result)>2:
	                                        if ((result[0]=='Image') & (result[1]=='coordinate')):                                             
	                                                xlis[cnt,i-1]=np.float(result[3])
	                                                ylis[cnt,i-1]=np.float(result[4])                                                

	                                        if ((result[0]=='Field') & (result[1]=='coordinate')):                                             
	                                                xlis_field[cnt,i-1]=np.float(result[3])
	                                                ylis_field[cnt,i-1]=np.float(result[4])                                                
	                                                
	
	                
	
	        cnt=cnt+1
	        #plt.plot(arr_x,arr_y)
	
	
	#xlis=np.array(xlis)
	#ylis=np.array(ylis) 
	
	# length_arr=[]
	# angle_arr=[]
	for i in range(xlis.shape[1]):
	    # length=np.sqrt((xlis[0,i]- xlis[1,i])**2 + (ylis[0,i]- ylis[1,i])**2  )
	    # length_arr.append(length)
	    # plt.figure(1)
	    plt.plot(xlis[:,i],ylis[:,i])
	    # angle=math.atan2((-ylis[1,i]+ ylis[0,i]),(-xlis[1,i]+ xlis[0,i])) 
	    # angle=math.degrees(angle)  
	    # angle_arr.append(angle)
	                    
	plt.show()  
	plt.figure(1)
	plt.plot(xlis[:,i],ylis[:,i])
	plt.plot([-18.432,-18.432],[-18.432,18.432],c='r',linewidth=4)
	plt.plot([18.432,18.432],[-18.432,18.432],c='r',linewidth=4)
	plt.plot([-18.432,18.432],[-18.432,-18.432],c='r',linewidth=4)
	plt.plot([-18.432,18.432],[18.432,18.432],c='r',linewidth=4)
	plt.title('SCALES ' + prism_title_plot+ ' Prism trace')
	plt.xlabel('mm')
	plt.ylabel('mm') 
	fig.savefig(prism_title+'.png')
	table=np.array([xlis_field[0,:],ylis_field[0,:],xlis[0,:],ylis[0,:],xlis[1,:],ylis[1,:],xlis[2,:],ylis[2,:],xlis[3,:],ylis[3,:],xlis[4,:],ylis[4,:]])
	#np.savetxt(prism_title+'_trace.csv',np.transpose(table),fmt='%1.4f')
