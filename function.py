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
