import stl
from stl import mesh

your_mesh = mesh.Mesh.from_file('models/file.stl')
your_mesh.save('OUTPUT.stl',mode='UTF-8')