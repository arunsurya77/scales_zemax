import numpy as np

x=np.arange( -4.444448e-05, 4.444449e-05,(2*4.444448e-05/16))*-1
y=np.arange(-0.00004722226,0.00004722227,(2*0.00004722226/17))*-1



count=1
for y_val in y:
	x_arr=x
	y_arr=np.ones(len(x))*y_val
	fname_x=str(count)+'.0000_x.txt'
	fname_y=str(count)+'.0000_y.txt'
	np.savetxt(fname_x,x_arr)
	np.savetxt(fname_y,y_arr)
	count=count+1
