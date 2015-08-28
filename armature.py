import bge

class Armature(object):
    def __init__(self, name):
        self.armature_name = name

    def setScene(self, scene):
        self.scene = scene

    def getScene(self):
        return scene

class Bones(Armature):
    def __init__(self, name, armature_name):
        self.bone_name = name
        super(Bones, self).__init__(armature_name)

    def setNickname(self, name):
        self.nickname = name

    def bone_rotation(self, x, y, z):
        self.scene.objects.get(self.armature_name).channels[self.bone_name].rotation_mode = bge.logic.ROT_MODE_XYZ
        self.scene.objects.get(self.armature_name).channels[self.bone_name].rotation_euler = (x, y, z)
        self.scene.objects.get(self.armature_name).update()
        
        
    


        
