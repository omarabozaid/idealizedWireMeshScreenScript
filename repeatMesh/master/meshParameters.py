import numpy as np
import matplotlib.pyplot as plt
import os

rf=1
phi=np.linspace(0.25,0.9,2)
lf=np.copy(phi)*0.0

for i in range(0,int(len(phi))):
    a=1
    b=4*rf/(phi[i]-1)
    c=4*rf*rf/(1-phi[i])
    lf[i]=(-b+pow(b*b-4*a*c,0.5))/(2*a)
    print(str(lf[i])+"   "+str(phi[i]))

fig = plt.figure()
plt.plot(phi,lf,"blue")
plt.xlabel("porosity $\phi$")
plt.ylabel("length of fiber $l_{fiber}$")
axes = plt.gca()
axes.set_xlim([0,1])
axes.set_ylim([rf,50*rf])
fig.savefig('porosityFiberLength.png')
os.system("display porosityFiberLength.png")
