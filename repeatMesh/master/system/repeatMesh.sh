maxX=5
lX=200
maxY=5
lY=200

cd master
#blockMesh
#snappyHexMesh

#rm -r ./constant/polyMesh
#cp -r ./3e-05/polyMesh ./constant/polyMesh

#rm -r 1e-05
#rm -r 2e-05
#rm -r 3e-05

fluentMeshToFoam semiMesh.msh
mirrorMesh -dict mirrorMeshDict.x -overwrite
mirrorMesh -dict mirrorMeshDict.y -overwrite
#mirrorMesh -dict mirrorMeshDict.z -overwrite
transformPoints -translate '(0 100 0)' 
topoSet
createPatch -overwrite
cd ..

for ((i=1;i<=maxX;i++))
do
	cp -r ./master ./'slave_'"$i"
	cd 'slave_'"$i"
	length=$(($lX*$i))
	transformPoints -translate '('"$length"' 0 0)'
	sed -i 's/PLANE1_0/PLANE1_'"$i"'/g' constant/polyMesh/boundary
	sed -i 's/PLANE4_0/PLANE4_'"$i"'/g' constant/polyMesh/boundary
	cd ..
done


for ((i=1;i<=maxX;i++))
do
	mergeMeshes master 'slave_'"$i" -overwrite
	cd master
	prevMesh=$(($i-1))
	stitchMesh 'PLANE4_'"$prevMesh" 'PLANE1_'"$i" -overwrite -perfect
	rm ./0/meshPhi
	cd ..
done

for ((i=1;i<=maxX;i++))
do
	rm -r 'slave_'"$i"
done


for ((i=1;i<=maxY;i++))
do
	cp -r ./master ./'slave_'"$i"
	cd 'slave_'"$i"
	length=$(($lY*$i))
	transformPoints -translate '(0 '"$length"' 0)'
	sed -i 's/PLANE5_0/PLANE5_'"$i"'/g' constant/polyMesh/boundary
	sed -i 's/PLANE6_0/PLANE6_'"$i"'/g' constant/polyMesh/boundary
	cd ..
done


for ((i=1;i<=maxY;i++))
do
	mergeMeshes master 'slave_'"$i" -overwrite
	cd master
	prevMesh=$(($i-1))
	stitchMesh 'PLANE6_'"$prevMesh" 'PLANE5_'"$i" -overwrite -perfect
	rm ./0/meshPhi
	cd ..
done

for ((i=1;i<=maxY;i++))
do
	rm -r 'slave_'"$i"
done


cd master
#transformPoints -scale '(1e-6 1e-6 1e-6)'
checkMesh > meshInformation.log
