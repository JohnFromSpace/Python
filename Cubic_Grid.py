import bpy

count = 100 

extents = 20.0

padding = 0.1

sz = (extents / count) - padding

iprc = 0.0
jprc = 0.0
kprc = 0.0
countf = 1.0 / (count - 1)
diff = extents * 2

z = 0.0
y = 0.0
x = 0.0

centerz = 0.0
centery = 0.0
centerx = 0.0

for i in range(0, count, 1):

    iprc = i * countf
    z = -extents + iprc * diff

    for j in range(0, count, 1):
        jprc = j * countf
        y = -extents + jprc * diff

        for k in range(0, count):
            kprc = k * countf
            x = -extents + kprc * diff

            bpy.ops.mesh.primitive_cube_add(location=(centerx + x, centery + y, centerz + z), radius=sz)

            current = bpy.context.object

            current.name = 'Cube ({0}, {1}, {2})'.format(k, j, i)
            current.data.name = 'Mesh ({0}, {1}, {2})'.format(k, j, i)

            mat = bpy.data.materials.new(name='Material ({0}, {1}, {2})'.format(k, j, i))

            mat.diffuse_color = (kprc, jprc, iprc)
            current.data.materials.append(mat)

bpy.ops.object.lamp_add(type='SUN', radius=1.0, location=(0.0, 0.0, extents * 0.667))

bpy.ops.object.camera_add(location=(extents * 1.414, extents * 1.414, extents * 2.121), rotation=(0.785398, 0.0, 2.35619))
bpy.context.object.data.type = 'ORTHO'
bpy.context.object.data.ortho_scale = extents * 7.0
