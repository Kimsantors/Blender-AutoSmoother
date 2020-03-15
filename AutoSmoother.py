#A script for applying auto smoothing and setting angle.

bl_info = {
    "name" : "AutoSmooth Normals",
    "author" : "kimsan",
    "description" : "A simple operator which enables smooth angles and sets the angle to 80.",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Object"
}

import bpy
from bpy import context

def main():   
    if bpy.context.active_object.type == 'MESH': 
        obj = bpy.context.selected_objects[0]
        obj.data.use_auto_smooth = 1
        obj.data.auto_smooth_angle = 1.3962633609771729
    

class AutoSmoother(bpy.types.Operator):
    bl_idname = "object.simple_operator"
    bl_label = "AutoSmooth"

    def execute(self, context):
        main()
        return {'FINISHED'}


def register():
    bpy.utils.register_class(AutoSmoother)


def unregister():
    bpy.utils.unregister_class(AutoSmoother)
    

    




    
    


