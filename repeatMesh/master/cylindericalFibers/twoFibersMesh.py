from readerFile import reader
from pointsFile import createPoints,createCenters,createSplines,createBoxPoints
from writer import writePoints,writeBlocks,writeEdges
from repeatMesh import repeatMesh

import numpy as np
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
import os


rf,lf,lOG,lCoarse,lFine,lDownWind=reader("inputDict.txt")

dTheta=45.0
nOGN=4
nOGT=3 #int(1.0*nOGN)
nF=5#int(0.25*(lf/lOG)*nOGN)

# print(rf)
# print(lf)
# print(lOG)
# print(lCoarse)
# print(lFine)
# print(lDownWind)

nFine=30#int((30.0/6.0)*15.0)#int((lFine/lf)*0.75*nF)
nCoarse=40#int(0.4*(30.0/6.0)*13.0)#int((lCoarse/lf)*0.75*nF)
nDownWind=30#int((18.0/6.0)*12.0)#int((lDownWind/lf)*0.55*nF)

print(nFine)
print(nCoarse)
print(nDownWind)

grading1=1#5
grading2=2#5
grading3=0.75#0.2

points=np.zeros((20,3))
normals=np.copy(points)
points,normals=createPoints(np.copy(points),np.copy(normals),lf,rf,lOG,dTheta)
boxCoarse,boxFine,BoxDownWind=createBoxPoints(points,lCoarse,lFine,lDownWind)

writePoints(points,boxFine,boxCoarse,BoxDownWind,"twoCylindericalFibersScript.txt")
centers=np.zeros((8,3))
centers=createCenters(rf,lf,lOG,dTheta)
splines=createSplines(rf,lOG,dTheta)
writeEdges(centers,splines,"twoCylindericalFibersScript.txt")
writeBlocks(nOGN,nOGT,nF,nFine,nCoarse,nDownWind,grading1,grading2,grading3,lCoarse,"twoCylindericalFibersScript.txt")

os.chdir("..")
os.system("cp ./cylindericalFibers/twoCylindericalFibersScript.txt ./system/.")
os.system("blockMesh")
os.system("sed -i 's/defaultFaces/COVERS/g' constant/polyMesh/boundary")
os.system("sed -i 's/empty/patch/g' constant/polyMesh/boundary")
os.chdir("..")

repeatMesh(4,lf,4,lf,lf,lFine+lCoarse,lDownWind,1)



#fig=plt.figure()
#ax=plt.gca(projection="3d")
#ax.scatter(points[:,0],points[:,1],points[:,2],marker='o')
#plt.show()
