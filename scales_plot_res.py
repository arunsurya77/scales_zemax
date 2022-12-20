import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import interpolate
w=np.array([2.0,3.0,4.0,5.0])
#ee=np.array([15.001787875729649,21.044259380810917,26.422641831858275,32.59364285134405])
#ee=np.array([16.330277624894677,22.026879920987085,27.455554062565284,33.85411624331084])
ee=np.array([38.33436835673703,37.33601051341695,38.053132592669236,41.451698195411865])

r=interpolate.interp1d(w,ee,fill_value='extrapolate')
fig = plt.figure(1)
ax = fig.add_subplot(111)

x_index=np.loadtxt('x_index.txt')
y_index=np.loadtxt('y_index.txt')
prism_index=4

prism_title_arr=['R80','R140','R250','R60','R35','R200']
prism_titleband_arr=['L-band','M-band','CH4/PAH','water ice','SEDs','K-band']
for p in range(6):

    prism_title=prism_title_arr[p]

    def ismissing(x,y):
       if np.logical_and(np.logical_and(x<1024,x>-1024),np.logical_and(y<1024,y>-1024)):
           return 0
       else:
           return 1

    xx=[]
    yy=[]
    arr=[]
    # fig = plt.figure(1)
    # ax = fig.add_subplot(111)
    # ax.set_xlim([-1148,1148])
    # ax.set_ylim([-1148,1148])
    count_in=0
    count_out=0


    #wave_samp=np.arange(1.9600,2.0604,.002)
    wave_samp=np.array([2.9000,4.1501])
    wave_samp=np.arange(2.9000,4.1500,0.2)
    #wave_samp=np.array([4.5000,5.2000])
    #wave_samp=np.arange(3.1000,3.5000,0.0501)


    wave_samp_arr=[]
    wave_samp_arr.append(np.arange(2.9000,4.1500,0.1000))#LBand
    wave_samp_arr.append(np.arange(4.5000,5.2000,0.1000))#Mband
    wave_samp_arr.append(np.arange(3.1000,3.5000,0.1000))#R250
    wave_samp_arr.append(np.arange(2.0000,3.7000,0.1000))#R60
    wave_samp_arr.append(np.arange(2.0000,5.000,0.1000))#R35
    wave_samp_arr.append(np.arange(1.9500,2.4500,0.1000))#R200
    wave_samp=wave_samp_arr[p]

    wave_samp_arr_plot=[]
    wave_samp_arr_plot.append(np.linspace(2.9000,4.1500,100))#LBand
    wave_samp_arr_plot.append(np.linspace(4.5000,5.2000,100))#Mband
    wave_samp_arr_plot.append(np.linspace(3.1000,3.5000,100))#R250
    wave_samp_arr_plot.append(np.linspace(2.0000,3.7000,100))#R60
    wave_samp_arr_plot.append(np.linspace(2.0000,5.000,100))#R35
    wave_samp_arr_plot.append(np.linspace(1.9500,2.4500,100))#R200
    #wave_samp=wave_samp_arr_plot[p]



    wave_len=len(wave_samp)
    xlis=np.zeros([wave_len,11881])
    ylis=np.zeros([wave_len,11881])
    miss_flag=np.zeros([109,109])
    cnt=0
    for j in wave_samp:
            arr_x=[]
            arr_y=[]
            if r(j)<36:
                pix_no=2
            else:
                pix_no=(r(j))/18
            #pix_no=2.
            for i in range(1,11882,1000): #
                    arr=[]
                    wave='{:01.4f}'.format(j)
                    filename= 'prism_'+prism_title+'_res/'+str(i)+'.0000'+wave
                    print(filename)
                    with open(filename) as f:
                            for line in f:
                                    result=line.split()
                                    if len(result)>2:
                                            #rint(result[0])
                                            if ((result[0]=='Image') & (result[1]=='coordinate')):
                                                    xx.append(np.float(result[3]))
                                                    yy.append(np.float(result[4]))
                                                    #print(result[3],result[4])
                                                    xlis[cnt,i-1]=np.float(result[3])*1000./18
                                                    ylis[cnt,i-1]=np.float(result[4])*1000./18

                                                    if ismissing(xlis[cnt,i-1],ylis[cnt,i-1])==1:
                                                        miss_flag[int(x_index[i-1])-1,int(y_index[i-1])-1]=1


                                                    arr_x.append(np.float(result[3])*1000./18)
                                                    arr_y.append(np.float(result[4])*1000/18)

                                                    arr.append(((np.float(result[3])*1000/15),(np.float(result[4])*1000/15)))

            arr_x=np.array(arr_x)
            arr_y=np.array(arr_y)
            cnt=cnt+1
            #plt.plot(arr_x,arr_y)


    #xlis=np.array(xlis)
    #ylis=np.array(ylis)

    # length_arr=[]
    # angle_arr=[]
    # for i in range(xlis.shape[1]):
    for i in range(1):#1000,11881,1000):
            res_arr=[]
            x=xlis[0,i]
            y=ylis[0,i]
            #print(x,y)
            for j in range(1,len(wave_samp)):
                    #print(xlis[j,i],ylis[j,i])
                    delt_pix=np.sqrt((xlis[j,i]- xlis[j-1,i])**2 + (ylis[j,i]- ylis[j-1,i])**2  )
                    delt_wave=wave_samp[j]-wave_samp[j-1]
                    delt_2pix=pix_no*(delt_wave/delt_pix)
                    res=wave_samp[j-1]/delt_2pix
                    res_arr.append(res)
                    print('hello',pix_no)
                    #print(res)
            #plt.plot(wave_samp[:-1],res_arr,label=str(x)+' '+str(y))
            f=np.polyfit(wave_samp[:-1],(res_arr),3)
            pol=np.poly1d(f)
            plt.plot(wave_samp_arr_plot[p],pol(wave_samp_arr_plot[p]),label=prism_titleband_arr[p],linewidth=5)
    # length=np.sqrt((xlis[0,i]- xlis[1,i])**2 + (ylis[0,i]- ylis[1,i])**2  )
    # length_arr.append(length)
    # #plt.scatter(xlis[0,i],ylis[0,i],c=length)
    # angle=math.atan2((-ylis[1,i]+ ylis[0,i]),(-xlis[1,i]+ xlis[0,i]))
    # angle=math.degrees(angle)
    # angle_arr.append(angle)

prism_title_arr=['K','L','M']
prism_titleband_arr=['K-midres','L-midres','M-midres']
for p in range(3):

    prism_title=prism_title_arr[p]

    def ismissing(x,y):
       if np.logical_and(np.logical_and(x<1024,x>-1024),np.logical_and(y<1024,y>-1024)):
           return 0
       else:
           return 1

    xx=[]
    yy=[]
    arr=[]
    # fig = plt.figure(1)
    # ax = fig.add_subplot(111)
    # ax.set_xlim([-1148,1148])
    # ax.set_ylim([-1148,1148])
    count_in=0
    count_out=0


    #wave_samp=np.arange(1.9600,2.0604,.002)
    wave_samp=np.array([2.9000,4.1501])
    wave_samp=np.arange(2.9000,4.1500,0.2)
    #wave_samp=np.array([4.5000,5.2000])
    #wave_samp=np.arange(3.1000,3.5000,0.0501)


    wave_samp_arr=[]
    wave_samp_arr.append(np.arange(1.9500,2.45,0.1000))#KBand
    wave_samp_arr.append(np.arange(2.9000,4.1500,0.1000))#LBand
    wave_samp_arr.append(np.arange(4.5000,5.2000,0.1000))#MBand
    wave_samp=wave_samp_arr[p]

    wave_samp_arr_plot=[]
    wave_samp_arr_plot.append(np.linspace(1.9500,2.45,100))#KBand
    wave_samp_arr_plot.append(np.linspace(2.9000,4.1500,100))#LBand
    wave_samp_arr_plot.append(np.linspace(4.5000,5.2000,100))#MBand
    #wave_samp=wave_samp_arr_plot[p]


    wave_len=len(wave_samp)
    xlis=np.zeros([wave_len,11881])
    ylis=np.zeros([wave_len,11881])
    miss_flag=np.zeros([109,109])
    cnt=0
    for j in wave_samp:
            arr_x=[]
            arr_y=[]
            if r(j)<36:
                pix_no=2
            else:
                pix_no=(r(j))/18
            #pix_no=2.
            for i in range(1,2,1): #
                    arr=[]
                    wave='{:01.4f}'.format(j)
                    filename= 'grating_'+prism_title+'_res/ls_1.0000_10.0000_'+wave+'.dat'
                    print(filename)
                    with open(filename) as f:
                            for line in f:
                                    result=line.split()
                                    #print(line)
                                    if len(result)>2:
                                            #print('inside',result[0])
                                            if ((result[0]=='Image') & (result[1]=='coordinate')):
                                                    #print('inside2')
                                                    xx.append(np.float(result[3]))
                                                    yy.append(np.float(result[4]))
                                                    #print(result[3],result[4])
                                                    #print('hello',cnt,i-1)
                                                    xlis[cnt,i-1]=np.float(result[3])*1000./18
                                                    ylis[cnt,i-1]=np.float(result[4])*1000./18

                                                    if ismissing(xlis[cnt,i-1],ylis[cnt,i-1])==1:
                                                        miss_flag[int(x_index[i-1])-1,int(y_index[i-1])-1]=1


                                                    arr_x.append(np.float(result[3])*1000./18)
                                                    arr_y.append(np.float(result[4])*1000/18)

                                                    arr.append(((np.float(result[3])*1000/15),(np.float(result[4])*1000/15)))

            #print('hello',arr_x)
            arr_x=np.array(arr_x)
            arr_y=np.array(arr_y)
            cnt=cnt+1
            #plt.plot(arr_x,arr_y)


    #xlis=np.array(xlis)
    #ylis=np.array(ylis)

    # length_arr=[]
    # angle_arr=[]
    # for i in range(xlis.shape[1]):
    for i in range(1):#1000,11881,1000):
            res_arr=[]
            x=xlis[0,i]
            y=ylis[0,i]
            #print(x,y)
            for j in range(1,len(wave_samp)):
                    #print(xlis[j,i],ylis[j,i])
                    delt_pix=np.sqrt((xlis[j,i]- xlis[j-1,i])**2 + (ylis[j,i]- ylis[j-1,i])**2  )
                    delt_wave=wave_samp[j]-wave_samp[j-1]
                    delt_2pix=pix_no*(delt_wave/delt_pix)
                    print('hello',pix_no)
                    res=wave_samp[j-1]/delt_2pix
                    res_arr.append(res)
                    print(res)
            #plt.plot(wave_samp[:-1],res_arr,label=str(x)+' '+str(y))
            f=np.polyfit(wave_samp[:-1],(res_arr),3)
            pol=np.poly1d(f)
            plt.plot(wave_samp_arr_plot[p],pol(wave_samp_arr_plot[p]),label=prism_titleband_arr[p],linewidth=5)
    # length=np.sqrt((xlis[0,i]- xlis[1,i])**2 + (ylis[0,i]- ylis[1,i])**2  )
    # length_arr.append(length)
    # #plt.scatter(xlis[0,i],ylis[0,i],c=length)
    # angle=math.atan2((-ylis[1,i]+ ylis[0,i]),(-xlis[1,i]+ xlis[0,i]))
    # angle=math.degrees(angle)
    # angle_arr.append(angle)


plt.show()
# plt.plot([-1024,-1024],[-1024,1024],c='r',linewidth=4)
# plt.plot([1024,1024],[-1024,1024],c='r',linewidth=4)
# plt.plot([-1024,1024],[-1024,-1024],c='r',linewidth=4)
# plt.plot([-1024,1024],[1024,1024],c='r',linewidth=4)
plt.title('Resolution across SCALES filters ',fontsize='large', fontweight='bold')
plt.xlabel('Wavelength (microns)',fontsize='large', fontweight='bold')
plt.ylabel('R',fontsize='large', fontweight='bold')
plt.legend()
ax.set_yscale('log')
plt.ylim([0,10000])
