import bpy
import random

space = 2.2
for i in range (30):
    for j in range(30):
        location = (i*space, j*space, random.random() * 2)
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, location=location)
        bpy.context.object.rotation_euler[0] = random.random()
        bpy.context.object.rotation_euler[1] = random.random()
        bpy.context.object.rotation_euler[2] = random.random()
        
        # Require to create a material before running the script
        item = bpy.context.object
        if random.random() < 0.1 :
            item.data.materials.append(bpy.data.materials['Material.001'])
        if random.random() > 0.1 and random.random() < 0.3 :
            item.data.materials.append(bpy.data.materials['Material.002'])
        if random.random() > 0.3 and random.random() < 0.4 :
            item.data.materials.append(bpy.data.materials['Material.003'])
        if random.random() > 0.4 and random.random() < 0.7 :
            item.data.materials.append(bpy.data.materials['Material.004'])
