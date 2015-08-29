
bonesList = [[],[]]

def rotate(rotationsList, armature):
    for x in range(0,24):
            armature.bone_rotation(bonesList[0][x], bonesList[1][x], rotationsList[x]) 
