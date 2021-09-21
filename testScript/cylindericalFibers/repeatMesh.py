import os
import numpy as np

def repeatMesh(maxX,lX,maxY,lY,lf,lUpWind,lDownWind,scaleFactor):
    os.system("rm -r repeatMesh")
    os.system("mkdir repeatMesh")
    os.system("cp -r testScript/ repeatMesh/master")
    os.chdir("repeatMesh/master/")
    mirrorAndTopoSet(lf,lUpWind,lDownWind)
    os.system("mirrorMesh -dict mirrorMeshDict.x -overwrite")
    os.system("mirrorMesh -dict mirrorMeshDict.y -overwrite")
    #os.system("transformPoints -translate '(0 " +str(0.0*lY)+" 0)'")
    os.system("topoSet")
    os.system("createPatch -overwrite")
    os.chdir("..")
    repeatX(maxX,lX)
    repeatY(maxY,lY)
    os.chdir("master")
    os.system("checkMesh > meshInformation.log")
    os.system("transformPoints -scale '("+str(scaleFactor)+" "+str(scaleFactor)+" "+str(scaleFactor)+" )'")


def mirrorAndTopoSet(lf,lUpWind,lDownWind):

    os.chdir("system/")
    outputFile=open("mirroredPointX.H","w")
    outputFile.write(" point   ("+str(0.5*lf)+" 0 0); \n")
    outputFile.close()

    outputFile=open("mirroredPointY.H","w")
    outputFile.write(" point   (0 "+str(0.5*lf)+" 0); \n")
    outputFile.close()

#    outputFile=open("f0.H","w")
#    outputFile.write(" box (-0.05 -0.05 "+str(-1.001*lDownWind)+") ("+str(1.001*lf)+" "+str(1.001*lf)+" "+str(-0.999*lDownWind)+"); \n")
    str0=" box (-0.05 -0.05 "+str(-1.001*lDownWind)+") ("+str(1.001*lf)+" "+str(1.001*lf)+" "+str(-0.999*lDownWind)+");"
#    outputFile.close()
#    outputFile=open("f1.H","w")
#    outputFile.write(" box (-0.05 -0.05 "+str(0.999*lUpWind)+") ("+str(1.001*lf)+" "+str(1.001*lf)+" "+str(1.001*lUpWind)+"); \n")
    str1=" box (-0.05 -0.05 "+str(0.999*lUpWind)+") ("+str(1.001*lf)+" "+str(1.001*lf)+" "+str(1.001*lUpWind)+");"
#    outputFile.close()
#    outputFile=open("f2.H","w")
#    outputFile.write(" box (-0.05 -0.05 "+str(-1.001*lDownWind)+") (0.05 "+" "+str(1.001*lf)+" "+str(1.001*lUpWind)+"); \n")
    str2=" box (-0.05 -0.05 "+str(-1.001*lDownWind)+") (0.05 "+" "+str(1.001*lf)+" "+str(1.001*lUpWind)+");"
#    outputFile.close()
#    outputFile=open("f3.H","w")
#    outputFile.write(" box ("+str(0.999*lf)+" -0.05 "+str(-1.001*lDownWind)+") ("+str(1.001*lf) +" "+str(1.001*lf)+" "+str(1.001*lUpWind)+"); \n")
    str3=" box ("+str(0.999*lf)+" -0.05 "+str(-1.001*lDownWind)+") ("+str(1.001*lf) +" "+str(1.001*lf)+" "+str(1.001*lUpWind)+");"
#    outputFile.close()
#    outputFile=open("f4.H","w")
#    outputFile.write(" box (-0.05 -0.05 "+str(-1.001*lDownWind)+") ("+str(1.001*lf)+" 0.05 "+str(1.001*lUpWind)+"); \n")
    str4=" box (-0.05 -0.05 "+str(-1.001*lDownWind)+") ("+str(1.001*lf)+" 0.05 "+str(1.001*lUpWind)+");"
#    outputFile.close()
#    outputFile=open("f5.H","w")
#    outputFile.write(" box (-0.05 "+str(0.999*lf)+" "+str(-1.001*lDownWind)+") ("+str(1.001*lf) +" "+str(1.001*lf)+" "+str(1.001*lUpWind)+"); \n")
    str5=" box (-0.05 "+str(0.999*lf)+" "+str(-1.001*lDownWind)+") ("+str(1.001*lf) +" "+str(1.001*lf)+" "+str(1.001*lUpWind)+");"
#    outputFile.close()

    os.chdir("..")
    os.system("sed -i 's/face0/"+str0+"/g' system/topoSetDict")
    os.system("sed -i 's/face1/"+str1+"/g' system/topoSetDict")
    os.system("sed -i 's/face2/"+str2+"/g' system/topoSetDict")
    os.system("sed -i 's/face3/"+str3+"/g' system/topoSetDict")
    os.system("sed -i 's/face4/"+str4+"/g' system/topoSetDict")
    os.system("sed -i 's/face5/"+str5+"/g' system/topoSetDict")

def repeatX(maxX,lX):
    for i in range(1,maxX+1):
        os.system("cp -r master/ slave_"+str(i))
        os.chdir("slave_"+str(i))
        length=lX*i
        os.system("transformPoints -translate '(" +str(length)+" 0 0)'")
        os.system("sed -i 's/PLANE1_0/PLANE1_"+str(i)+"/g' constant/polyMesh/boundary")
        os.system("sed -i 's/PLANE4_0/PLANE4_"+str(i)+"/g' constant/polyMesh/boundary")
        os.chdir("..")

    for i in range(1,maxX+1):
        os.system("mergeMeshes master slave_"+str(i)+" -overwrite")
        os.chdir("master")
        prevMesh=i-1
        os.system("stitchMesh PLANE4_"+str(prevMesh)+" PLANE1_"+str(i)+" -overwrite -perfect")
        os.system("rm ./0/meshPhi")
        os.chdir("..")

    for i in range(1,maxX+1):
        os.system("rm -r slave_"+str(i))

def repeatY(maxY,lY):
    for i in range(1,maxY+1):
        print(maxY+1)
        os.system("cp -r master/ slave_"+str(i))
        os.chdir("slave_"+str(i))
        length=lY*i
        os.system("transformPoints -translate '(0 " +str(length)+" 0)'")
        os.system("sed -i 's/PLANE5_0/PLANE5_"+str(i)+"/g' constant/polyMesh/boundary")
        os.system("sed -i 's/PLANE6_0/PLANE6_"+str(i)+"/g' constant/polyMesh/boundary")
        os.chdir("..")

    for i in range(1,maxY+1):
        os.system("mergeMeshes master slave_"+str(i)+" -overwrite")
        os.chdir("master")
        prevMesh=i-1
        os.system("stitchMesh PLANE6_"+str(prevMesh)+" PLANE5_"+str(i)+" -overwrite -perfect")
        os.system("rm ./0/meshPhi")
        os.chdir("..")

    for i in range(1,maxY+1):
        os.system("rm -r slave_"+str(i))

