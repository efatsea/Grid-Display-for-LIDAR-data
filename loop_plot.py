import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import csv
import pandas as pd
import numpy as np
from mpltools import special
import scipy.integrate as integrate
from scipy.integrate import simps
from numpy import trapz
import glob

#------- Filter function fixed(list, sens)------------
# Apply this function in a list you like to filter and return a new list without noice and with the same size. 
# sens is from sensitivity and is by default 20 but for the ext plot it needs to be around 2. 
#--------------------Examples-----------------
# ax5.plot(fixed(ext,2),height,color='black',label='ext')
# ax3.plot(fixed(s355nf),height,color='lightblue',label='S355nf')

new=[]
def fixed(list,sens=25):
	new = []
	for x in range(len(list)):
		if list[x]>list[x-1]+sens or list[x]<list[x-1]-sens:
			new.append(None)
		else:
			new.append(list[x])
	return new
#---------------------------------------------------

def plot_func(file):
	data = np.loadtxt(file, skiprows=1)
	height = np.loadtxt(file, skiprows=1, usecols=0)
	heightt=np.array(height)
	h1=heightt.tolist().index(1.003176)
	h12=heightt.tolist().index(1.204905)
	h15=heightt.tolist().index(1.503764)
	h18=heightt.tolist().index(1.802622)
	h2=heightt.tolist().index(2.004351)
	h22=heightt.tolist().index(2.206081)
	h24=heightt.tolist().index(2.445167)
	h25=heightt.tolist().index(2.504939)
	h3=heightt.tolist().index(3.005527)
	h32=heightt.tolist().index(3.207256)
	h35=heightt.tolist().index(3.506115)
	h4=heightt.tolist().index(4.006703)
	h45=heightt.tolist().index(4.507291)
	h5=heightt.tolist().index(5.000407)
	h55=heightt.tolist().index(5.500995)
	h6=heightt.tolist().index(6.001583)
	h65=heightt.tolist().index(6.502170)
	h7=heightt.tolist().index(7.002758)
	h75=heightt.tolist().index(7.503346)
	h8=heightt.tolist().index(8.003934)
	h85=heightt.tolist().index(8.504522)
	h9=heightt.tolist().index(9.005110)
	h12=heightt.tolist().index(12.001165)

	b355 = np.loadtxt(file, skiprows=1, usecols=1)
	b355er = np.loadtxt(file, skiprows=1, usecols=2)
	b532 = np.loadtxt(file, skiprows=1, usecols=3)
	b532er = np.loadtxt(file, skiprows=1, usecols=4)
	b1064 = np.loadtxt(file, skiprows=1, usecols=5)
	b1064er = np.loadtxt(file, skiprows=1, usecols=6)
	b355nf = np.loadtxt(file, skiprows=1, usecols=60)
	b355nfer = np.loadtxt(file, skiprows=1, usecols=61)
	b532nf = np.loadtxt(file, skiprows=1, usecols=39)
	b532nfer = np.loadtxt(file, skiprows=1, usecols=40)
	a355nf = np.loadtxt(file, skiprows=1, usecols=62)
	a532nf = np.loadtxt(file, skiprows=1, usecols=41)
	a355 = np.loadtxt(file, skiprows=1, usecols=7)
	a532 = np.loadtxt(file, skiprows=1, usecols=9)
	s355nf = np.loadtxt(file, skiprows=1, usecols=64)
	s532nf = np.loadtxt(file, skiprows=1, usecols=43)
	s355 = np.loadtxt(file, skiprows=1, usecols=11)
	s532 = np.loadtxt(file, skiprows=1, usecols=13)
	vd532 = np.loadtxt(file, skiprows=1, usecols=22)
	pd532 = np.loadtxt(file, skiprows=1, usecols=25)
	vd355 = np.loadtxt(file, skiprows=1, usecols=31)
	pd355 = np.loadtxt(file, skiprows=1, usecols=34)
	b355_532 = np.loadtxt(file, skiprows=1, usecols=17)
	b532_1064 = np.loadtxt(file, skiprows=1, usecols=19)
	ext = np.loadtxt(file, skiprows=1, usecols=15)

	#-------Calculate the inetgrations---------------
	#intt532a= a532nf[0:h2]
	#intt532b= a532[h2:h12]
	#intt532=np.append(intt532a,intt532b)
	#intt355a= a355nf[0:h2]
	#intt355b= a355[h2:h12]
	#intt355=np.append(intt355a,intt355b)
	#int355 = np.trapz(intt355)/1000
	#int532 = np.trapz(intt532)/1000
	#print(int355,' int355')
	#print(int532,' int532')

	#AOD calculation------------------------------------------------------------------------------------
	## Compute the area using the composite trapezoidal rule.
	area_a355_trapz = np.trapz(a355[0:2197], height[0:2197]*0.001)
	print("area_a355_trapz =", area_a355_trapz)

	area_a532_trapz = np.trapz(a532[0:2197], height[0:2197]*0.001)
	print("area_a532_trapz =", area_a532_trapz)
	a355_all = np.append(a355nf[0:107],a355[107:2197])
	a532_all = np.append(a532nf[0:107],a532[107:2197])

	## Compute the area using the composite Simpson's rule.
	area_a355_simps = simps(a355_all[0:2197], height[0:2197]*0.001)
	AOD_355 = round(area_a355_simps,2)
	print("AOD_355 =", AOD_355)

	area_a532_simps = simps(a532_all[0:2197], height[0:2197]*0.001)
	AOD_532 = round(area_a532_simps,2)
	print("AOD_532 =", AOD_532)


	#setup figure and sublots
	fig1 = plt.figure(constrained_layout=True,figsize=(12,5))
	spec = gridspec.GridSpec(ncols=5, nrows=1)
	ax1 = fig1.add_subplot(spec[0, 0])
	ax2 = fig1.add_subplot(spec[0, 1])
	ax3 = fig1.add_subplot(spec[0, 2])
	ax4 = fig1.add_subplot(spec[0, 3])
	ax5 = fig1.add_subplot(spec[0, 4])
	fig1.suptitle(file[6:20], fontsize=16)

	ytick = [0,1,2,3,4,5,6,7,8,9,10]
	ylimits = [0,10]
	#-----------Backscatter Coefficient------------------


	ax1.plot(fixed(b355nf),height,color='lightblue',label='b355nf')
	#special.errorfill(b355nf,height,b355nfer,color='lightblue',alpha_fill=0.4,ax=ax1)
	ax1.plot(fixed(b532nf),height,color='lightgreen',label='b532nf')
	#special.errorfill(b532nf,height,b532nfer,color='lightgreen',alpha_fill=0.4,ax=ax1)
	ax1.plot(fixed(b355),height,color='blue',label='b355')
	#special.errorfill(b355,height,b355er,color='blue',alpha_fill=0.2,ax=ax1)
	ax1.plot(fixed(b532),height,color='green',label='b532')
	#special.errorfill(b532,height,b532er,color='green',alpha_fill=0.2,ax=ax1)
	ax1.plot(fixed(b1064),height,color='red',label='b1064')
	#special.errorfill(b1064,height,b1064er,color='red',alpha_fill=0.4,ax=ax1)

	ax1.set_xlim([0,3])
	ax1.set_xticks([1,2,3])
	ax1.set_ylim(ylimits)
	ax1.set_yticks(ytick)
	ax1.legend(fontsize='small')
	ax1.grid(True,)
	ax1.set_title('Backscatter Coefficient',fontsize='small')
	ax1.set_xlabel('β (Mm^-1 sr^-1)',fontsize='small')
	ax1.set_ylabel('Height(km)',fontsize='small')
	for tick in ax1.xaxis.get_ticklabels():
	    tick.set_fontsize('small')
	for tick in ax1.yaxis.get_ticklabels():
	    tick.set_fontsize('small')
	    

	#---------------Extinction Coefficient-----------------
	ax2.plot(fixed(a355nf),height,color='lightblue',label='a355nf')
	ax2.plot(fixed(a532nf),height,color='lightgreen',label='a532nf')
	ax2.plot(fixed(a355),height,color='blue',label='a355')
	ax2.plot(fixed(a532),height,color='green',label='a532')

	ax2.legend(fontsize='small')
	ax2.set_xlim([0,125])
	ax2.set_xticks([0,25,50,75,100,125])
	ax2.set_ylim(ylimits)
	ax2.set_yticks(ytick)
	ax2.grid(True)
	ax2.set_title('Extinction Coefficient',fontsize='small')
	ax2.set_xlabel('a (Mm^-1)',fontsize='small')
	for tick in ax2.xaxis.get_ticklabels():
	    tick.set_fontsize('small')
	for tick in ax2.yaxis.get_ticklabels():
	    tick.set_fontsize('small')

	#--------------------Lidar Ratio------------------------
	ax3.plot(fixed(s532nf),height,color='lightgreen',label='S532nf')
	ax3.plot(fixed(s355nf),height,color='lightblue',label='S355nf')
	ax3.plot(fixed(s355),height,color='blue',label='S355')
	ax3.plot(fixed(s532),height,color='green',label='S532')

	ax3.legend(fontsize='small')
	ax3.set_xlim([0,150])
	ax3.set_xticks([0,50,100,150])
	ax3.set_ylim(ylimits)
	ax3.set_yticks(ytick)
	ax3.grid(True)
	ax3.set_title('Lidar Ratio',fontsize='small')
	ax3.set_xlabel('LR(sr)',fontsize='small')
	for tick in ax3.xaxis.get_ticklabels():
	    tick.set_fontsize('small')
	for tick in ax3.yaxis.get_ticklabels():
	    tick.set_fontsize('small')

	#-------------------Depolarization--------------------------
	ax4.plot(fixed(pd355),height,color='lightblue',label='PD355')
	ax4.plot(fixed(pd532),height,color='lightgreen',label='PD532')
	ax4.plot(fixed(vd355),height,color='blue',label='VD355')
	ax4.plot(fixed(vd532),height,color='green',label='VD532')

	ax4.legend(fontsize='small')
	ax4.set_xlim([0,0.2])
	ax4.set_xticks([0,0.05,0.1,0.15,0.2,])
	ax4.set_ylim(ylimits)
	ax4.set_yticks(ytick)
	ax4.grid(True)
	ax4.set_title('Depolarization',fontsize='small')
	ax4.set_xlabel('δ',fontsize='small')
	for tick in ax4.xaxis.get_ticklabels():
	    tick.set_fontsize('xx-small')
	for tick in ax4.yaxis.get_ticklabels():
	    tick.set_fontsize('small')

	#--------------------Angstrom Exponent-----------------------
	ax5.plot(fixed(b355_532),height,color='blue',label='b(355/532)')
	ax5.plot(fixed(b532_1064),height,color='red',label='b(532/1064)')
	ax5.plot(fixed(ext,3),height,color='black',label='ext')
	

	ax5.legend(fontsize='small')
	ax5.set_xlim([-6,6])
	ax5.set_xticks([-6,-4,-2,0,2,4,6])
	ax5.set_ylim(ylimits)
	ax5.set_yticks(ytick)
	ax5.grid(True)
	ax5.set_title('Angstrom Exponent',fontsize='small')
	ax5.set_xlabel('AE',fontsize='small')
	for tick in ax5.xaxis.get_ticklabels():
	    tick.set_fontsize('small')
	for tick in ax5.yaxis.get_ticklabels():
	    tick.set_fontsize('small')
	#---------------------------------------------------------------
	fig1.savefig(file[6:20]+'.png')


#----------------LOOP FOR MANY PLOTS IN A FILE CALLED 'FILLES'-------------------

#i= 0;
#files = glob.glob("files/*.txt")
#for x in files:	
#	file = x
#	i+=1
#	string=str(i)
#	plot_func(file)
#---------------------------------------------------------------------------------

file = '23 2-3r-20180923_200 AM-258 AM-71smooth'+'.txt'
plot_func(file)


