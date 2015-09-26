import csv

bonesList = [["Thumb2_R", "Thumb2_R", "Thumb3_R", "Thumb3_R", "Thumb4_R", "Index2_R", "Index2_R", "Index3_R", "Index4_R", "Middle2_R", "Middle2_R", "Middle3_R", "Middle4_R", "Ring2_R", "Ring2_R", "Ring3_R", "Ring3_R", "Ring4_R", "Ring5_R", "Pinky2_R", "Pinky2_R", "Pinky3_R", "Pinky3_R", "Pinky4_R", "Pinky5_R"],[ "z", "x", "z", "x", "z", "z", "x", "x", "x", "z", "x", "x", "x", "z", "x", "z", "x", "x", "x", "z", "x", "z", "x", "x", "x"]]

frame = 0
fileReader = []

def openFile(file_name):
    with open(file_name) as csvfile:
        file1 = csv.reader(csvfile, delimiter=';')
        global fileReader
        for row in file1:
            fileReader.append(row)

def rotate(armature):
    global frame
    for x in range(0,25):  
        armature.bone_rotation(bonesList[0][x], bonesList[1][x], fileReader[frame + 2][x + 19])

    if frame >= 388:
        frame = 0
        print(reset)
    frame += 1
    

    

    
