import numpy as np
import matplotlib.pyplot as plt
import re
import math
import matplotlib.cm as cm
import matplotlib.patches as patches


wave_samp=[1.95]
fig = plt.figure(1)
ax = fig.add_subplot(111)
#ax.set_xlim([-25,25])
#ax.set_ylim([-25,25])
arr_x=[]
arr_y=[]
rms_arr=[]
data= np.loadtxt('zemaxlogK_angle3.txt')

x=data[:,0]
y=data[:,1]

for i in range(0,1,1):
	xx=x[i*2000:(i+1)*2000]
	yy=y[i*2000:(i+1)*2000]
	ind=np.where(np.logical_and(np.logical_and(xx<22,xx>-22) , np.logical_and(yy<22,yy>-22)))
	xx=xx[ind]
	yy=yy[ind]
	xc=np.mean(xx)
	yc=np.mean(yy)
	#xc=xx[0]
	#yc=yy[0]
	rad_arr=np.sqrt(np.mean((xc-xx)**2+(yc-yy)**2))*1000
	rms_arr.append(rad_arr)
	#rms_arr.append(rms[0])
	arr_x.append(xc)
	arr_y.append(yc)
	plt.figure()
	plt.scatter(xx,yy)
	plt.show()
	rad_arr=rad_arr*0.001
	plt.xlim([xc-2*rad_arr,xc+2*rad_arr])
	plt.ylim([yc-2*rad_arr,yc+2*rad_arr])	
	plt.pause(1)
	

arr_x=np.array(arr_x)
arr_y=np.array(arr_y)
rms_arr=np.array(rms_arr)
plt.scatter(arr_x,arr_y,c=rms_arr,cmap='jet')
plt.plot([-18.432,-18.432],[-18.432,18.432],c='r',linewidth=4)
plt.plot([18.432,18.432],[-18.432,18.432],c='r',linewidth=4)
plt.plot([-18.432,18.432],[-18.432,-18.432],c='r',linewidth=4)
plt.plot([-18.432,18.432],[18.432,18.432],c='r',linewidth=4)
plt.title('RMS spot Size over Detector R200 Kband EoE ')
plt.show()
plt.colorbar()
# plt.gca().invert_xaxis()
# plt.plot([-2048,2048],[-2048,-2048],c='r')
# plt.plot([-2048,2048],[2048,2048],c='r')
# plt.plot([-2048,-2048],[-2048,2048],c='r')
# plt.plot([2048,2048],[-2048,2048],c='r')
