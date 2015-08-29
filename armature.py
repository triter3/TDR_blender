import bge

class Armature():
    def __init__(self, name, scene):
        self.armature_name = name
        self.scene = scene
    
    def getScene(self):
        return scene

    def bone_rotation(self, bone_name, orientation, angle):
        if orientation == "x":
            self.scene.objects.get(self.armature_name).channels[bone_name].rotation_mode = bge.logic.ROT_MODE_XYZ
            self.scene.objects.get(self.armature_name).channels[bone_name].rotation_euler = (angle, 0, 0)
            self.scene.objects.get(self.armature_name).update()

        if orientation == "y":
            self.scene.objects.get(self.armature_name).channels[bone_name].rotation_mode = bge.logic.ROT_MODE_XYZ
            self.scene.objects.get(self.armature_name).channels[bone_name].rotation_euler = (0, angle, 0)
            self.scene.objects.get(self.armature_name).update()

        if orientation== "z":
            self.scene.objects.get(self.armature_name).channels[bone_name].rotation_mode = bge.logic.ROT_MODE_XYZ
            self.scene.objects.get(self.armature_name).channels[bone_name].rotation_euler = (0, 0, angle)
            self.scene.objects.get(self.armature_name).update()
            



        
        
        
    


        
