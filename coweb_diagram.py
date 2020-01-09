import matplotlib.pyplot as plt
import numpy as np
import pdb

""" Input Parameters """
r, map_iterates, init, cycle_times = 0.885, 3, 0.1, 100

""" Graphing Variables """
f_x, x_ax, index, cycle_x, cycle_y = [0]*101, [0]*101, 0, [0]*cycle_times, [0]*cycle_times

""" Cycle Map Graph """
for i in range(0,101,1):
	x_n, x_ax[index] = i/100, i/100

	for itr in range(0,map_iterates):
		x_n = 4*r*(x_n)*(1-(x_n))

	f_x[index] = x_n
	index+=1

""" Projection """
proj = np.linspace(0,1,num=101)

""" Cycle Path """
for step in range(0,cycle_times):
	if (step%2 == 0 and step != 0):
		cycle_x[step] = cycle_y[step-1]
		cycle_y[step]  = cycle_y[step-1]

	elif (step == 0):
		cycle_x[step] = init
		cycle_y[step] = init

	else:
		next_y = cycle_x[step-1]
		for itr in range(0,map_iterates):
			next_y = 4*r*(next_y)*(1-(next_y))
		cycle_y[step] = next_y
		#print(cycle_y[step])
		cycle_x[step] = cycle_x[step-1]

""" Setting Up Graphs """
fig = plt.figure()
ax1 = plt.axes()
ax2 = plt.axes()
ax3 = plt.axes()

ax1.set_xlim([0,1])
ax1.set_ylim([0,1])
ax1.plot(x_ax, f_x)

ax2.plot(x_ax, proj)

ax3.plot(cycle_x, cycle_y)

plt.show()