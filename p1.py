#animacoes em matplot

import numpy as np 
from matplotlib import pyplot as plt
from matplotlib import animation
import math

w=[10]
the=[0.]
a=[0.]
at=[0.]
wt=[0.]
t=[0.]
e=[0.]
de=[0.]
dt=0.01
m=1
l=10
g=9.8
gama=0.3


for tt in range(10000):

   the.append((the[-1]+w[-1]*dt+0.5*a[-1]*dt**2))
   at.append(-(w[0]**2)*math.sin(the[-1]) - gama*w[-1])
   wt.append(w[-1]+0.5*(a[-1]+at[-1])*dt)
   at.append(-(wt[0]**2)*math.sin(the[-1]) - gama*wt[-1])
   w.append(w[-1]+0.5*(a[-1]+at[-1])*dt)
   a.append(-(w[0]**2)*math.sin(the[-1])-gama*w[-1])
   t.append(t[-1]+dt)
   e.append((w[-1]**2)/2 + m*g*(l-l*math.cos(the[-1])))
   

y = np.asarray(the)
t = np.asarray(t)
v = np.asarray(w)
en = np.asarray(e)
posx = -np.cos(y)*l
posy = np.sin(y)*l
#animate

fig = plt.figure()
plt.rc('text', usetex=True) 
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.subplots_adjust(hspace=1)

xxt = fig.add_subplot(341,xlim=(0,25), ylim=(-5,5))
plt.title(r'\textit{Posi\c{c}\~ao $\times$ t}', fontsize=16)
line1, = xxt.plot([],[],'g',lw=0.8)


wxt = fig.add_subplot(345,xlim=(0,25), ylim=(-10,10))
plt.title(r'\textit{W $\times$ t}', fontsize=16)
line2, = wxt.plot([],[],'r-',lw=0.8)

ext = fig.add_subplot(349,xlim=(0,25), ylim=(0,100))
plt.title(r'\textit{Energy}', fontsize=16)
line3, = ext.plot([],[],lw=0.8)

fase = fig.add_subplot(144, xlim=(min(y)-0.1, max(y)+0.1), ylim=(min(v)-0.1,max(v)+0.1))
plt.title(r'\textit{Espa\c{c}o de fase}', fontsize=18)
line4, = fase.plot([],[],'b',lw=0.8)
plt.xlabel(r'\textit{$x$}')
plt.ylabel(r'\textit{$v$}')

pend = fig.add_subplot(132, xlim=(-l*1.1,l*1.1), ylim=(-l*1.1,l*1.1),aspect='equal')
plt.title(r'\textit{$\omega_0 = 10, \gamma = 0.3$, l = 10, m = 1}', fontsize=18)
line5, = pend.plot([],[],'ko-',lw=1)
plt.xlabel(r'\textit{$x$}')
plt.ylabel(r'\textit{$y$}')


#plot inicial pro blitting
def init():
	line1.set_data([],[])
	line2.set_data([],[])
	line3.set_data([],[])
	line4.set_data([],[])
	line5.set_data([],[])
	return line1, line2, line3, line4, line5,
	
def animate(i):
	massx = [0,posx[i]]
	massy = [0,posy[i]]
	line1.set_data(t[:i],y[:i])
	line2.set_data(t[:i],v[:i])
	line3.set_data(t[:i],e[:i])
	line4.set_data(y[:i],v[:i])
	line5.set_data(massy,massx)
	return line1, line2, line3, line4, line5,

	
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=t.size, interval=0, blit=True,repeat=False)
#anim.save('pendwatri.mp4')
plt.show()
