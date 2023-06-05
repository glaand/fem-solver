import numpy as np
import pyvista as pv
from modules.mesh_cube import Mesh as CubeMesh
from modules.mesh_bar import Mesh as BarMesh
from modules.mesh_box import Mesh as BoxMesh
from modules.assembly import Assembly
from modules.solver import Solver

mesh = BoxMesh()

nodes = mesh.get_nodes().T
faces = mesh.get_faces()
mesh = pv.PolyData(mesh.get_nodes(), faces)

mesh.plot(show_edges=True, line_width=5, color="w", show_scalar_bar=False)