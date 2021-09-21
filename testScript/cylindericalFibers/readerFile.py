#Reader
import ast
def reader(fileName):
	with open(fileName,"r") as data:
		dictionary=ast.literal_eval(data.read())

	rf=float(dictionary.get('rf'))
	lf=float(dictionary.get('lf'))
	lOG=float(dictionary.get('lOG'))
	lCoarse=float(dictionary.get('lCoarse'))
	lFine=float(dictionary.get('lFine'))
	lDownWind=float(dictionary.get('lDownWind'))

	if(lFine==-1):
		lFine=4*lf
	if(lDownWind==-1):
		lDownWind=4*lf
	if (lOG==-1):
		lOA=lf-2*rf
		lOG=0.25*lOA

	return rf,lf,lOG,lCoarse,lFine,lDownWind
