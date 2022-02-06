import bpy
from math import pi, sin, cos
import colorsys
from random import TWOPI

# Center of sphere.
centerz = 0.0
centery = 0.0
centerx = 0.0

# Sphere diameter.
diameter = 10.0

sz = 5.0 / diameter

latitude = 20
longitude = latitude * 2

invlatitude = 1.0 / (latitude - 1)
invlongitude = 1.0 / (longitude - 1)
iprc = 0.0
jprc = 0.0
phi = 0.0
theta = 0.0

for i in range(0, latitude, 1):
    iprc = i * invlatitude
    phi = pi * (i + 1) * invlatitude
    
    sinphi = sin(phi)
    cosphi = cos(phi)
    
    rad = 0.1 + sz * abs(sinphi) * 1
    z = cosphi * diameter

    for j in range(0, longitude, 1):
        jprc = j * invlongitude
        theta = TWOPI * j / longitude

        sintheta = sin(theta)
        costheta = cos(theta)

        x = sinphi * costheta * diameter
        y = sinphi * sintheta * diameter

        bpy.ops.mesh.primitive_cube_add(location=(centerx + x, centery + y, centerz + z), radius=rad)

        current = bpy.context.object

        current.name = 'Cube ({0:0>2d}, {1:0>2d})'.format(i, j)
        current.data.name = 'Mesh ({0:0>2d}, {1:0>2d})'.format(i, j)

        current.rotation_euler = (0.0, phi, theta)

        mat = bpy.data.materials.new(name='Material ({0:0>2d}, {1:0>2d})'.format(i, j))

        mat.diffuse_color = colorsys.hsv_to_rgb(jprc, 1.0 - iprc, 1.0)
        current.data.materials.append(mat)
