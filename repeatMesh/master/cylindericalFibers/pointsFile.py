import math
import numpy as np
from myTrigFunctions import cosDeg, sinDeg, tanDeg

def oGrid(point_,normal_,length_):
	return point_+normal_*length_

def createPoints(points,normals,lf,rf,lOG,dTheta):
	for i in range(0,3):
		points[i][0]=0.5*lf
		points[i][1]=rf*cosDeg(i*dTheta)
		points[i][2]=rf*sinDeg(i*dTheta)
		normals[i][0]=0
		normals[i][1]=cosDeg(i*dTheta)
		normals[i][2]=sinDeg(i*dTheta)
	for i in range(3,6):
		points[i]=oGrid(np.copy(points[i-3]),np.copy(normals[i-3]),lOG)
		normals[i]=normals[i-6]

	for i in range(6,9):
		points[i][0]=points[i-6][1]
		points[i][1]=points[i-6][1]
		points[i][2]=pow(rf*rf-points[i-6][1]*points[i-6][1],0.5)
		normals[i][0]=1
		if (points[i-6][1]==rf):
			normals[i][2]=0
		else:
			normals[i][2]=points[i-6][1]/pow(rf*rf-points[i-6][1]*points[i-6][1],0.5)
		normals[i][1]=1
		normals[i]=normals[i]/np.linalg.norm(normals[i])

	for i in range(9,12):
		points[i][0]=(rf+lOG)*cosDeg((i-9)*dTheta)
		points[i][1]=(rf+lOG)*cosDeg((i-9)*dTheta)
		points[i][2]=pow(pow(rf+lOG,2)-pow(points[i][1],2),0.5)
		normals[i][0]=1
		if (points[i-6][1]==rf+lOG):
			normals[i][2]=0
		else:
			normals[i][2]=points[i][1]/pow((rf+lOG)*(rf+lOG)-points[i][1]*points[i][1],0.5)
		normals[i][1]=1
		normals[i]=normals[i]/np.linalg.norm(normals[i])

	for i in range(12,15):
		points[i][0]=rf*cosDeg((i-12)*dTheta)
		points[i][1]=0.5*lf
		points[i][2]=rf*sinDeg((i-12)*dTheta)
		normals[i][0]=cosDeg((i-12)*dTheta)
		normals[i][1]=0
		normals[i][2]=sinDeg((i-12)*dTheta)

	for i in range(15,18):
		points[i]=oGrid(np.copy(points[i-3]),np.copy(normals[i-3]),lOG)
		normals[i]=normals[i-6]

	points[18][0]=0.5*lf
	points[18][1]=0.5*lf
	points[18][2]=0.0

	points[19][0]=0.5*lf
	points[19][1]=0.5*lf
	points[19][2]=points[4][2]


	return points,normals

def createCenters(rf,lf,lOG,dTheta):
	center=np.zeros((8,3))

	center[0][0]=0.5*lf
	center[0][1]=rf*cosDeg(dTheta/2)
	center[0][2]=rf*sinDeg(dTheta/2)

	center[1][0]=0.5*lf
	center[1][1]=(rf+lOG)*cosDeg(dTheta/2)
	center[1][2]=(rf+lOG)*sinDeg(dTheta/2)

	center[2][0]=0.5*lf
	center[2][1]=rf*cosDeg(3*dTheta/2)
	center[2][2]=rf*sinDeg(3*dTheta/2)

	center[3][0]=0.5*lf
	center[3][1]=(rf+lOG)*cosDeg(3*dTheta/2)
	center[3][2]=(rf+lOG)*sinDeg(3*dTheta/2)

	center[4][0]=rf*cosDeg(dTheta/2)
	center[4][1]=0.5*lf
	center[4][2]=rf*sinDeg(dTheta/2)

	center[5][0]=(rf+lOG)*cosDeg(dTheta/2)
	center[5][1]=0.5*lf
	center[5][2]=(rf+lOG)*sinDeg(dTheta/2)

	center[6][0]=rf*cosDeg(3*dTheta/2)
	center[6][1]=0.5*lf
	center[6][2]=rf*sinDeg(3*dTheta/2)

	center[7][0]=(rf+lOG)*cosDeg(3*dTheta/2)
	center[7][1]=0.5*lf
	center[7][2]=(rf+lOG)*sinDeg(3*dTheta/2)

	return center

def createSplines(rf,lOG,dTheta):
	splines=[]

	spline=np.zeros((10,3))
	y=np.linspace(rf,rf*cosDeg(dTheta),10)
	for i in range(0,10):
		spline[i][0]=y[i]
		spline[i][1]=y[i]
		spline[i][2]=pow(rf*rf-y[i]*y[i],0.5)
	splines.append(np.copy(spline))

	spline=np.zeros((10,3))
	y=np.linspace(rf*cosDeg(dTheta),0,10)
	for i in range(0,10):
		spline[i][0]=y[i]
		spline[i][1]=y[i]
		spline[i][2]=pow(rf*rf-y[i]*y[i],0.5)
	splines.append(np.copy(spline))

	spline=np.zeros((10,3))
	y=np.linspace(rf+lOG,(rf+lOG)*cosDeg(dTheta),10)
	for i in range(0,10):
		spline[i][0]=y[i]
		spline[i][1]=y[i]
		spline[i][2]=pow((rf+lOG)*(rf+lOG)-y[i]*y[i],0.5)
	splines.append(np.copy(spline))

	spline=np.zeros((10,3))
	y=np.linspace((rf+lOG)*cosDeg(dTheta),0,10)
	for i in range(0,10):
		spline[i][0]=y[i]
		spline[i][1]=y[i]
		spline[i][2]=pow((rf+lOG)*(rf+lOG)-y[i]*y[i],0.5)
	splines.append(np.copy(spline))

	splines=np.asarray(splines)
	return splines

def createBoxPoints(points_,lCoarse,lFine,lDownWind):
	faceCoarse_=np.zeros((7,3))
	faceFine_=np.zeros((7,3))
	faceDownWind_=np.zeros((7,3))

	faceFine_[0][0]=points_[11][0]
	faceFine_[0][1]=points_[11][1]
	faceFine_[0][2]=lFine

	faceFine_[1][0]=points_[5][0]
	faceFine_[1][1]=points_[5][1]
	faceFine_[1][2]=lFine

	faceFine_[2][0]=points_[4][0]
	faceFine_[2][1]=points_[4][1]
	faceFine_[2][2]=lFine

	faceFine_[3][0]=points_[10][0]
	faceFine_[3][1]=points_[10][1]
	faceFine_[3][2]=lFine

	faceFine_[4][0]=points_[19][0]
	faceFine_[4][1]=points_[19][1]
	faceFine_[4][2]=lFine

	faceFine_[5][0]=points_[16][0]
	faceFine_[5][1]=points_[16][1]
	faceFine_[5][2]=lFine

	faceFine_[6][0]=points_[17][0]
	faceFine_[6][1]=points_[17][1]
	faceFine_[6][2]=lFine
##
	faceCoarse_[0][0]=points_[11][0]
	faceCoarse_[0][1]=points_[11][1]
	faceCoarse_[0][2]=lFine+lCoarse

	faceCoarse_[1][0]=points_[5][0]
	faceCoarse_[1][1]=points_[5][1]
	faceCoarse_[1][2]=lFine+lCoarse

	faceCoarse_[2][0]=points_[4][0]
	faceCoarse_[2][1]=points_[4][1]
	faceCoarse_[2][2]=lFine+lCoarse

	faceCoarse_[3][0]=points_[10][0]
	faceCoarse_[3][1]=points_[10][1]
	faceCoarse_[3][2]=lFine+lCoarse

	faceCoarse_[4][0]=points_[19][0]
	faceCoarse_[4][1]=points_[19][1]
	faceCoarse_[4][2]=lFine+lCoarse

	faceCoarse_[5][0]=points_[16][0]
	faceCoarse_[5][1]=points_[16][1]
	faceCoarse_[5][2]=lFine+lCoarse

	faceCoarse_[6][0]=points_[17][0]
	faceCoarse_[6][1]=points_[17][1]
	faceCoarse_[6][2]=lFine+lCoarse
##
	faceDownWind_[0][0]=points_[11][0]
	faceDownWind_[0][1]=points_[11][1]
	faceDownWind_[0][2]=-lDownWind

	faceDownWind_[1][0]=points_[5][0]
	faceDownWind_[1][1]=points_[5][1]
	faceDownWind_[1][2]=-lDownWind

	faceDownWind_[2][0]=points_[4][0]
	faceDownWind_[2][1]=points_[4][1]
	faceDownWind_[2][2]=-lDownWind

	faceDownWind_[3][0]=points_[10][0]
	faceDownWind_[3][1]=points_[10][1]
	faceDownWind_[3][2]=-lDownWind

	faceDownWind_[4][0]=points_[19][0]
	faceDownWind_[4][1]=points_[19][1]
	faceDownWind_[4][2]=-lDownWind

	faceDownWind_[5][0]=points_[16][0]
	faceDownWind_[5][1]=points_[16][1]
	faceDownWind_[5][2]=-lDownWind

	faceDownWind_[6][0]=points_[17][0]
	faceDownWind_[6][1]=points_[17][1]
	faceDownWind_[6][2]=-lDownWind


	return faceCoarse_,faceFine_,faceDownWind_
