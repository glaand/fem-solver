import numpy as np
import pyvista as pv
from modules.mesh_cube import Mesh as CubeMesh
from modules.mesh_bar import Mesh as BarMesh
from modules.mesh_box import Mesh as BoxMesh
from modules.assembly import Assembly
from modules.solver import Solver

plotter = pv.Plotter(shape=(1, 2))

mesh = BoxMesh()
nodes = mesh.get_nodes()
faces = mesh.get_faces()
plotter.subplot(0, 0)
plotter.add_text("Before deformation", font_size=20)
plotter.add_mesh(pv.PolyData(nodes, faces), color='white', show_edges=True)

# Displacement figure
assembly = Assembly(mesh)
assembly.assemble_global_stiffness_matrix()
assembly.apply_boundary_conditions()
solver = Solver(assembly)
U = solver.solve()
U = assembly.solution_tensor_to_matrix(U)
mesh.set_displacements(U)

nodes = mesh.get_displaced_nodes()
faces = mesh.get_faces()
plotter.subplot(0, 1)
plotter.add_text("After deformation", font_size=20)
plotter.add_mesh(pv.PolyData(nodes, faces), color='white', show_edges=True)

plotter.show()