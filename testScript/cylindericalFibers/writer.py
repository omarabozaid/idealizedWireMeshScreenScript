import numpy as np

def writePoints(p,pFine,pCoarse,pDownWind,fileName):
	outputFile=open(fileName,"w")
	outputFile.write("vertices \n")
	outputFile.write("( \n")
	for i in range(0,int(len(p))):
		outputFile.write("//point no. "+str(i)+"\n")
		outputFile.write(str('(')+str(p[i][0])+str(' ')+str(p[i][1])+str(' ')+str(p[i][2])+str(' )\n'))
	for i in range(0,int(len(p))):
		outputFile.write("//point no. "+str(int(len(p)+i))+"\n")
		outputFile.write(str('(')+str(p[i][0])+str(' ')+str(p[i][1])+str(' ')+str(-p[i][2])+str(' )\n'))
	for i in range(0,int(len(pFine))):
		outputFile.write("//point no. "+str(2*int(len(p)+i))+"\n")
		outputFile.write(str('(')+str(pFine[i][0])+str(' ')+str(pFine[i][1])+str(' ')+str(pFine[i][2])+str(' )\n'))
	for i in range(0,int(len(pCoarse))):
		outputFile.write("//point no. "+str(2*int(len(p)+int(len(pFine))+i))+"\n")
		outputFile.write(str('(')+str(pCoarse[i][0])+str(' ')+str(pCoarse[i][1])+str(' ')+str(pCoarse[i][2])+str(' )\n'))
	for i in range(0,int(len(pDownWind))):
		outputFile.write("//point no. "+str(2*int(len(p))+int(len(pFine)+len(pCoarse))+i)+"\n")
		outputFile.write(str('(')+str(pDownWind[i][0])+str(' ')+str(pDownWind[i][1])+str(' ')+str(pDownWind[i][2])+str(' )\n'))
	outputFile.write(str('); \n'))
	outputFile.close()

def writeBlocks(nOGN,nOGT,nF,nFine,nCoarse,nDownWind,grading1,grading2,grading3,lCoarse,fileName):
	outputFile=open(fileName,"a")
	outputFile.write("blocks \n")
	outputFile.write("( \n")
	outputFile.write(str('hex (6 0 3 9 7 1 4 10) fluid ('+str(nF)+' '+str(nOGN)+' '+str(nOGT)+') simpleGrading (1 1 1) \n'))
	outputFile.write(str('hex (7 1 4 10 8 2 5 11) fluid ('+str(nF)+' '+str(nOGN)+' '+str(nOGT)+') simpleGrading (1 1 1) \n'))
	outputFile.write(str('hex (6 9 15 12 7 10 16 13) fluid ('+str(nOGN)+' '+str(nF)+' '+str(nOGT)+') simpleGrading (1 1 1) \n'))
	outputFile.write(str('hex (7 10 16 13 8 11 17 14) fluid ('+str(nOGN)+' '+str(nF)+' '+str(nOGT)+') simpleGrading (1 1 1) \n'))
	outputFile.write(str('hex (9 3 18 15 10 4 19 16) fluid ('+str(nF)+' '+str(nF)+' '+str(nOGT)+') simpleGrading (1 1 1) \n'))

	outputFile.write(str('hex (27 21 24 30 26 20 23 29 ) fluid ('+str(nF)+' '+str(nOGN)+' '+str(nOGT)+') simpleGrading (1 1 1) \n'))
	outputFile.write(str('hex (28 22 25 31 27 21 24 30 ) fluid ('+str(nF)+' '+str(nOGN)+' '+str(nOGT)+') simpleGrading (1 1 1) \n'))
	outputFile.write(str('hex (27 30 36 33 26 29 35 32 ) fluid ('+str(nOGN)+' '+str(nF)+' '+str(nOGT)+') simpleGrading (1 1 1) \n'))
	outputFile.write(str('hex (28 31 37 34 27 30 36 33 ) fluid ('+str(nOGN)+' '+str(nF)+' '+str(nOGT)+') simpleGrading (1 1 1) \n'))
	outputFile.write(str('hex (30 24 39 36 29 23 38 35 ) fluid ('+str(nF)+' '+str(nF)+' '+str(nOGT)+') simpleGrading (1 1 1) \n'))

	outputFile.write(str('hex (11 5 4 10 40 41 42 43 ) fluid ('+str(nF)+' '+str(nOGT)+' '+str(nFine)+') simpleGrading (1 1 '+str(grading1)+' ) \n'))
	outputFile.write(str('hex (10 4 19 16 43 42 44 45 ) fluid ('+str(nF)+' '+str(nF)+' '+str(nFine)+') simpleGrading (1 1 '+str(grading1)+' ) \n'))
	outputFile.write(str('hex (11 10 16 17 40 43 45 46 ) fluid ('+str(nOGT)+' '+str(nF)+' '+str(nFine)+') simpleGrading (1 1 '+str(grading1)+' ) \n'))

	outputFile.write(str('hex (54 55 56 57 31 25 24 30 ) fluid ('+str(nF)+' '+str(nOGT)+' '+str(nDownWind)+') simpleGrading (1 1 '+str(grading3)+' ) \n'))
	outputFile.write(str('hex (57 56 58 59 30 24 39 36 ) fluid ('+str(nF)+' '+str(nF)+' '+str(nDownWind)+') simpleGrading (1 1 '+str(grading3)+' ) \n'))
	outputFile.write(str('hex (54 57 59 60 31 30 36 37 ) fluid ('+str(nOGT)+' '+str(nF)+' '+str(nDownWind)+') simpleGrading (1 1 '+str(grading3)+' ) \n'))

	if(lCoarse>0):
		outputFile.write(str('hex (40 41 42 43 47 48 49 50 ) fluid ('+str(nF)+' '+str(nOGT)+' '+str(nCoarse)+') simpleGrading (1 1 '+str(grading2)+' ) \n'))
		outputFile.write(str('hex (43 42 44 45 50 49 51 52 ) fluid ('+str(nF)+' '+str(nF)+' '+str(nCoarse)+') simpleGrading (1 1 '+str(grading2)+' ) \n'))
		outputFile.write(str('hex (40 43 45 46 47 50 52 53 ) fluid ('+str(nOGT)+' '+str(nF)+' '+str(nCoarse)+') simpleGrading (1 1 '+str(grading2)+' ) \n'))


	outputFile.write(str('); \n'))
	outputFile.close()

def writeEdges(centers,splines,fileName):
	outputFile=open(fileName,"a")
	outputFile.write("edges \n")
	outputFile.write("( \n")
	outputFile.write(str('arc 0 1 ')+str('(')+str(centers[0][0])+str(' ')+str(centers[0][1])+str(' ')+str(centers[0][2])+str(' )\n'))
	outputFile.write(str('arc 1 2 ')+str('(')+str(centers[2][0])+str(' ')+str(centers[2][1])+str(' ')+str(centers[2][2])+str(' )\n'))
	outputFile.write(str('arc 12 13 ')+str('(')+str(centers[4][0])+str(' ')+str(centers[4][1])+str(' ')+str(centers[4][2])+str(' )\n'))
	outputFile.write(str('arc 13 14 ')+str('(')+str(centers[6][0])+str(' ')+str(centers[6][1])+str(' ')+str(centers[6][2])+str(' )\n'))

	outputFile.write(str('arc 3 4 ')+str('(')+str(centers[1][0])+str(' ')+str(centers[1][1])+str(' ')+str(centers[1][2])+str(' )\n'))
	outputFile.write(str('arc 4 5 ')+str('(')+str(centers[3][0])+str(' ')+str(centers[3][1])+str(' ')+str(centers[3][2])+str(' )\n'))
	outputFile.write(str('arc 15 16 ')+str('(')+str(centers[5][0])+str(' ')+str(centers[5][1])+str(' ')+str(centers[5][2])+str(' )\n'))
	outputFile.write(str('arc 16 17 ')+str('(')+str(centers[7][0])+str(' ')+str(centers[7][1])+str(' ')+str(centers[7][2])+str(' )\n'))

	outputFile.write(str('spline 6 7 \n'))
	outputFile.write(str('( \n'))
	spline=np.copy(splines[0])
	for i in range(0,len(spline)):
		outputFile.write(str('(')+str(spline[i][0])+str(' ')+str(spline[i][1])+str(' ')+str(spline[i][2])+str(' ) \n'))
	outputFile.write(str(') \n'))

	outputFile.write(str('spline 7 8 \n'))
	outputFile.write(str('( \n'))
	spline=np.copy(splines[1])
	for i in range(0,len(spline)):
		outputFile.write(str('(')+str(spline[i][0])+str(' ')+str(spline[i][1])+str(' ')+str(spline[i][2])+str(' ) \n'))
	outputFile.write(str(') \n'))

	outputFile.write(str('spline 9 10 \n'))
	outputFile.write(str('( \n'))
	spline=np.copy(splines[2])
	for i in range(0,len(spline)):
		outputFile.write(str('(')+str(spline[i][0])+str(' ')+str(spline[i][1])+str(' ')+str(spline[i][2])+str(' ) \n'))
	outputFile.write(str(') \n'))

	outputFile.write(str('spline 10 11 \n'))
	outputFile.write(str('( \n'))
	spline=np.copy(splines[3])
	for i in range(0,len(spline)):
		outputFile.write(str('(')+str(spline[i][0])+str(' ')+str(spline[i][1])+str(' ')+str(spline[i][2])+str(' ) \n'))
	outputFile.write(str(') \n'))

	outputFile.write(str('arc 20 21 ')+str('(')+str(centers[0][0])+str(' ')+str(centers[0][1])+str(' ')+str(-centers[0][2])+str(' )\n'))
	outputFile.write(str('arc 21 22 ')+str('(')+str(centers[2][0])+str(' ')+str(centers[2][1])+str(' ')+str(-centers[2][2])+str(' )\n'))
	outputFile.write(str('arc 32 33 ')+str('(')+str(centers[4][0])+str(' ')+str(centers[4][1])+str(' ')+str(-centers[4][2])+str(' )\n'))
	outputFile.write(str('arc 33 34 ')+str('(')+str(centers[6][0])+str(' ')+str(centers[6][1])+str(' ')+str(-centers[6][2])+str(' )\n'))

	outputFile.write(str('arc 23 24 ')+str('(')+str(centers[1][0])+str(' ')+str(centers[1][1])+str(' ')+str(-centers[1][2])+str(' )\n'))
	outputFile.write(str('arc 24 25 ')+str('(')+str(centers[3][0])+str(' ')+str(centers[3][1])+str(' ')+str(-centers[3][2])+str(' )\n'))
	outputFile.write(str('arc 35 36 ')+str('(')+str(centers[5][0])+str(' ')+str(centers[5][1])+str(' ')+str(-centers[5][2])+str(' )\n'))
	outputFile.write(str('arc 36 37 ')+str('(')+str(centers[7][0])+str(' ')+str(centers[7][1])+str(' ')+str(-centers[7][2])+str(' )\n'))

	outputFile.write(str('spline 26 27 \n'))
	outputFile.write(str('( \n'))
	spline=np.copy(splines[0])
	for i in range(0,len(spline)):
		outputFile.write(str('(')+str(spline[i][0])+str(' ')+str(spline[i][1])+str(' ')+str(-spline[i][2])+str(' ) \n'))
	outputFile.write(str(') \n'))

	outputFile.write(str('spline 27 28 \n'))
	outputFile.write(str('( \n'))
	spline=np.copy(splines[1])
	for i in range(0,len(spline)):
		outputFile.write(str('(')+str(spline[i][0])+str(' ')+str(spline[i][1])+str(' ')+str(-spline[i][2])+str(' ) \n'))
	outputFile.write(str(') \n'))

	outputFile.write(str('spline 29 30 \n'))
	outputFile.write(str('( \n'))
	spline=np.copy(splines[2])
	for i in range(0,len(spline)):
		outputFile.write(str('(')+str(spline[i][0])+str(' ')+str(spline[i][1])+str(' ')+str(-spline[i][2])+str(' ) \n'))
	outputFile.write(str(') \n'))

	outputFile.write(str('spline 30 31 \n'))
	outputFile.write(str('( \n'))
	spline=np.copy(splines[3])
	for i in range(0,len(spline)):
		outputFile.write(str('(')+str(spline[i][0])+str(' ')+str(spline[i][1])+str(' ')+str(-spline[i][2])+str(' ) \n'))
	outputFile.write(str(') \n'))

	outputFile.write(str('); \n'))
	outputFile.close()
