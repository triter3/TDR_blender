import bge
import math

class Armature():
    def __init__(self, name, scene):
        self.armature_name = name
        self.scene = scene
        self.first_angle = 0
        self.double_loop = False
    
    def getScene(self):
        return scene

    def bone_rotation(self, bone_name, orientation, angle1):
        angle = angle1.replace(",",".")
        angle = float(angle)
        angle = angle * (math.pi/180)
        print("angle")
        if orientation == "x":
            angle = angle * (-1)
            self.scene.objects.get(self.armature_name).channels[bone_name].rotation_mode = bge.logic.ROT_MODE_XYZ
            self.scene.objects.get(self.armature_name).channels[bone_name].rotation_euler = (angle, 0, 0)
            self.scene.objects.get(self.armature_name).update()

        if orientation == "y":
            self.scene.objects.get(self.armature_name).channels[bone_name].rotation_mode = bge.logic.ROT_MODE_XYZ
            self.scene.objects.get(self.armature_name).channels[bone_name].rotation_euler = (0, angle, 0)
            self.scene.objects.get(self.armature_name).update()

        if orientation == "z":
            self.scene.objects.get(self.armature_name).channels[bone_name].rotation_mode = bge.logic.ROT_MODE_XYZ
            self.scene.objects.get(self.armature_name).channels[bone_name].rotation_euler = (0, 0, angle)
            self.scene.objects.get(self.armature_name).update()
        
        if orientation == "xz":
            if self.double_loop == False:
                self.first_angle = angle
                self.double_loop = True
            elif self.double_loop == True:
                print(self.first_angle)
                self.scene.objects.get(self.armature_name).channels[bone_name].rotation_mode = bge.logic.ROT_MODE_XYZ
                self.scene.objects.get(self.armature_name).channels[bone_name].rotation_euler = (self.first_angle, 0, angle)
                self.scene.objects.get(self.armature_name).update()
                self.double_loop = False

        if orientation == "zx":
            if self.double_loop == False:
                self.first_angle = angle
                self.double_loop = True
            elif self.double_loop == True:
                print(self.first_angle)
                self.scene.objects.get(self.armature_name).channels[bone_name].rotation_mode = bge.logic.ROT_MODE_XYZ
                self.scene.objects.get(self.armature_name).channels[bone_name].rotation_euler = (angle, 0, self.first_angle)
                self.scene.objects.get(self.armature_name).update()
                self.double_loop = False