
bonesList = [["Thumb2_R", "Thumb2_R", "Thumb3_R", "Thumb3_R", "Thumb4_R", "Index2_R", "Index2_R", "Index3_R", "Index4_R", "Middle2_R", "Middle2_R", "Middle3_R", "Middle4_R", "Ring2_R", "Ring2_R", "Ring3_R", "Ring3_R", "Ring4_R", "Ring5_R", "Pinky2_R", "Pinky2_R", "Pinky3_R", "Pinky3_R", "Pinky4_R", "Pinky5_R"],[ "x", "z", "x", "z", "x", "z", "x", "x", "x", "z", "x", "x", "x", "z", "x", "z", "x", "x", "x", "z", "x", "z", "x", "x", "x"]]

def rotate(rotationsList, armature):
    for x in range(0,24):
            armature.bone_rotation(bonesList[0][x], bonesList[1][x], rotationsList[x]) 
